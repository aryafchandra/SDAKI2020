from sys import stdin


class VaccineMaterial:
    def __init__(self, name, quality_rating):
        self.name = name
        self.quality_rating = quality_rating


class MaterialWithStock():
    def __init__(self, material, stock):
        self.material = material
        self.stock = stock


class VaccineFormula:
    def __init__(self, formula_sequence, vaccinematerial_sequence):
        self.formula_sequence = formula_sequence
        self.vaccinematerial_sequence = vaccinematerial_sequence


class Vaccine:
    def __init__(self, name, quality_rating, medical_trial_cost):
        self.name = name
        self.quality_rating = quality_rating
        self.medical_trial_cost = medical_trial_cost
        self.is_in_bank = False


class Factory:
    def __init__(self, name, materials_with_stock = None):
        self.materials_with_stock = materials_with_stock
        if materials_with_stock == None:
            materials_with_stock = []
        self.name = name
        self.vaccine_warehouse = []


    def produce_vaccine(self, name, vaccine_formula):
        medical_trial_cost = sum(vaccine_formula.formula_sequence)
        quantityMaterialSum = 0
        for i in range(len(vaccine_formula.formula_sequence)):
            if self.materials_with_stock[i].stock < vaccine_formula.formula_sequence[i]:
                raise Exception("Not enough material for " + self.materials_with_stock[i].material.name)
        for i in range(len(vaccine_formula.formula_sequence)):
            self.materials_with_stock[i].stock -= vaccine_formula.formula_sequence[i]
            quantityMaterialSum += vaccine_formula.formula_sequence[i] * vaccine_formula.vaccinematerial_sequence[i].quality_rating
        quality_score = (quantityMaterialSum % 1000) + 1
        return Vaccine(name, quality_score, medical_trial_cost)
    



def lexi_compare(str1, str2):
    to_check = 0
    if len(str1) <= len(str2):
        to_check = len(str1)
    if len(str1) > len(str2):
        to_check = len(str2)
    for i in range(to_check):
        if ord(str1[i]) < ord(str2[i]):
            return 0
        if ord(str1[i]) > ord(str2[i]):
            return 1
    return -1



def vaccine_quick_sort_partition(vaccines, start, end):
    i = start - 1
    pivot = vaccines[end]
    for j in range(start, end):
        if vaccines[j].quality_rating > pivot.quality_rating:
            i = i+1
            vaccines[i], vaccines[j] = vaccines[j], vaccines[i]
        if vaccines[j].quality_rating == pivot.quality_rating:
            if vaccines[j].medical_trial_cost < pivot.medical_trial_cost:
                i = i+1
                vaccines[i], vaccines[j] = vaccines[j], vaccines[i]
            if vaccines[j].medical_trial_cost == pivot.medical_trial_cost:
                name_chars_check = list(vaccines[j].name)
                name_chars_pivot = list(pivot.name)
                lexi_check = lexi_compare(name_chars_check, name_chars_pivot)
                if lexi_check == 0: 
                    i = i+1
                    vaccines[i], vaccines[j] = vaccines[j], vaccines[i]


    vaccines[i+1], vaccines[end] = vaccines[end], vaccines[i+1]
    return i+1


def vaccine_quick_sort(vaccines, start, end):
    if len(vaccines) == 1:
        return vaccines
    if start < end:
        part = vaccine_quick_sort_partition(vaccines, start, end)
        vaccine_quick_sort(vaccines, start, part-1)
        vaccine_quick_sort(vaccines, part+1, end)


def vaccine_dynamic(vaccines, limit):
    qualities = list(map(lambda v: v.quality_rating, vaccines))
    trial = list(map(lambda v: v.medical_trial_cost, vaccines))

    
    dynamicTable = [[0 for x in range(limit + 1)] for x in range(len(vaccines) + 1)]


    for i in range(len(vaccines) + 1):
        for j in range(limit + 1):
            if i == 0 or j == 0:
                dynamicTable[i][j] = 0
            elif trial[i-1] <= j:
                dynamicTable[i][j] = max(qualities[i-1] + dynamicTable[i-1][j-trial[i-1]], dynamicTable[i-1][j])
            else:
                dynamicTable[i][j] = dynamicTable[i-1][j]

    return dynamicTable[len(qualities)][limit]


materials = []
factories = []
vaccine_bank = []
days_meta = []

n_material = int(stdin.readline())
for i in range(n_material):
    raw_in = stdin.readline().split()
    materials.append(VaccineMaterial(raw_in[0], int(raw_in[1])))

n_factories = int(stdin.readline())
for i in range(n_factories):
    factory = Factory(stdin.readline().split()[0], [])
    for j in range(n_material):
        raw_in = stdin.readline().split()
        material = list(filter(lambda m: m.name == raw_in[0], materials)) 
        factory.materials_with_stock.append(MaterialWithStock(material[0], int(raw_in[1])))
    factories.append(factory)

days = int(stdin.readline())
total_distributed_vaccines = 0
total_vaccines_produced = 0
for i in range(days):
    n_activities = int(stdin.readline())
    for j in range(n_activities):
        query = stdin.readline().split()
        factory = list(filter(lambda f: f.name == query[1], factories))[0]
         
        if query[0] == "RESTOCK":
            material = list(filter(lambda m: m.name == query[2], materials))[0] 
            quantity = int(query[3])
            factory_mws = list(filter(lambda mws: mws.material.name == material.name, factory.materials_with_stock))[0] 
            factory_mws.stock += quantity # tambah stoknya
        if query[0] == "PRODUCE":
            formula = VaccineFormula(list(map(lambda f: int(f), query[3:])), materials) 
            try:
                vaccine = factory.produce_vaccine(query[2], formula)  
                factory.vaccine_warehouse.append(vaccine) 
                total_vaccines_produced += 1
            except Exception: 
                pass
        if query[0] == "DISTRIBUTE":
            n_to_distribute = int(query[2])
            undistributed_vaccines = list(filter(lambda v: not v.is_in_bank, factory.vaccine_warehouse))
            if len(undistributed_vaccines) == 0: 
                pass
            if len(undistributed_vaccines) < n_to_distribute: 
                n_to_distribute = len(undistributed_vaccines)
            for k in range(n_to_distribute): 
                undistributed_vaccines[k].is_in_bank = True
                total_distributed_vaccines += 1
    days_meta.append([total_vaccines_produced, total_distributed_vaccines])
  
last_query = stdin.readline().split()
for i, day_meta in enumerate(days_meta):
    print("Hari ke-" + str(i+1) + ": " + str(day_meta[0]) + " " + str(day_meta[1]))
    
  
if last_query[0] == "CEK_KINERJA_PABRIK":
    for factory in factories:
        n_distributed_vaccines = len(list(filter(lambda v: v.is_in_bank, factory.vaccine_warehouse)))
        print(factory.name + " " + str(len(factory.vaccine_warehouse)) + " " + str(n_distributed_vaccines))
if last_query[0] == "CEK_SEMUA_VAKSIN":
    all_vaccines = []
    for factory in factories: 
        all_vaccines += factory.vaccine_warehouse
    vaccine_quick_sort(all_vaccines, 0, len(all_vaccines)-1) 
    for vaccine in all_vaccines:
        print(vaccine.name + " " + str(vaccine.quality_rating) + " " + str(vaccine.medical_trial_cost) + " " + ("TRUE" if vaccine.is_in_bank else "FALSE"))
if last_query[0] == "CEK_TOTAL_KUALITAS_UJICOBA":
    all_vaccines_in_bank = []
    for factory in factories:
        all_vaccines_in_bank += list(filter(lambda v: v.is_in_bank, factory.vaccine_warehouse)) 
    print(vaccine_dynamic(all_vaccines_in_bank, int(last_query[1])))
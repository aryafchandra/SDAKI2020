class List:
    def __init__(self): 
        self.tbl = []

    def insert(self, x, i):
        self.tbl.insert(i, x)
        
    def add(self,x):
        self.tbl.append(x)
        
    def remove(self, i):
        x = self.tbl[i]
        del self.tbl[i]
        return x
        
    def get(self, i):
        return self.tbl[i]

    def makeEpmty(self):
        self.tbl.clear()

    def size(self):
        return len(self.tbl)

    def print(self):
        print(self.tbl)
        
class Stack:
    def __init__(self): 
        self.tbl = []
        self.top = 0

    def push(self,X):
        self.tbl.append(X)
        self.top += 1
        
    def pop(self):
        if (self.top <= 0):
            return None
        self.top -= 1
        X = self.tbl[self.top]
        del self.tbl[self.top]
        return X
        
    def peek(self): 
        return self.tbl[self.top-1]
    
    def isEmpty(self): 
        return len(self.tbl) == 0

    def size(self): 
        return self.top

    def print(self):
        print(self.tbl)

class Queue:
    def __init__(self): 
        self.tbl = []

    def enqueue(self,X):
        self.tbl.append(X)
        
    def dequeue(self):
        X = self.tbl[0]
        del self.tbl[0]
        return X
        
    def peek(self): 
        return self.tbl[0]
    
    def isEmpty(self): 
        return len(self.tbl) == 0

    def size(self): 
        return len(self.tbl)

    def print(self):
        print(self.tbl)
        
class Set:
    def __init__(self): 
        self.tbl = []

    def add(self,a):
        self.tbl.add(a)
        
    def contains(self,a):
        return a in self.tbl

    def remove(self,a):
        self.tbl.remove(a)
        
    def size(self):
        return len(self.tbl)
    
    def print(self):
        print(self.tbl)

class Map:
    def __init__(self): 
        self.tbl = []

    def put(self,a,b):
        self.tbl[a] = b
        print(self.tbl)
    def get(self,a):
        return self.tbl[a]

    def remove(self,a):
        del self.tbl[a]
        print(self.tbl)
        
    def size(self):
        return len(self.tbl)
    def print(self):
        print(self.tbl)

class PriorityQueue:
    def __init__(self): 
        self.tbl = []

    def insert(self, x):
        i = len(self.tbl)-1
        while (i >= 0):
            if self.tbl[i] >= x:
                self.tbl.insert(i+1,x)
                return
            i -= 1
        self.tbl.insert(0,x)
            
    def pop(self):
        if len(self.tbl) > 0:
            x = self.tbl[0]
            del self.tbl[0]
            return x
        return None
        
    def peek(self):
        if len(self.tbl) > 0:
            return self.tbl[0]
        return None
    
    def isEmpty(self):
        return len(self.tbl) == 0
    
    def size(self):
        return len(self.tbl)
    
    def print(self):
        print(self.tbl)      

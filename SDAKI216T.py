# Graph Using Adjacency List
from sys import stdin
from collections import deque
import time as t

'''
Author       : Arya Fakhruddin Chandra
NPM          : 2006607526
Collaborator : YouTube Videos, Anastasia Audi, Alexander Caesario 
'''


class Graph:
    def __init__(self, vertex):
        self.adj_list = {vertex: [] for vertex in
                         range(vertex)}  # General, structure {Origin : [Type, Destinantion, Weight]}
        self.adj_list0 = {vertex: [] for vertex in range(vertex)}
        self.adj_list1 = []
        self.adj_list2 = {vertex: [] for vertex in range(vertex)}
        # Create Vertex

    def add_edge(self, tipe, origin, destination, weight=0):
        self.adj_list[origin].append([tipe, destination, weight])

        if tipe == 0:
            self.adj_list0[origin].append([destination, weight])
            self.adj_list0[destination].append([origin, weight])

            self.adj_list[destination].append([tipe, origin, weight])

        elif tipe == 1:
            self.adj_list1.append([origin, destination, destination, origin])

            self.adj_list[destination].append([tipe, origin, weight])

        elif tipe == 2:
            self.adj_list2[origin].append([destination])

    def delete_edge(self, tipe, origin, destination):
        temp_origin_list = self.adj_list[origin]
        temp_destination_list = self.adj_list[destination]
        if tipe == 0:
            temp_origin_list0 = self.adj_list0[origin]
            temp_destination_list0 = self.adj_list0[destination]
            for x in temp_origin_list0:
                if x[0] == destination:
                    self.adj_list0[origin].remove(x)
                    break

            for y in temp_destination_list0:
                if y[0] == origin:
                    self.adj_list0[destination].remove(y)
                    break

            for z in temp_origin_list:
                if z[0] == 0 and z[1] == destination:
                    self.adj_list[origin].remove(z)
                    break

            for zz in temp_destination_list:
                if zz[0] == 0 and zz[1] == origin:
                    self.adj_list[destination].remove(zz)
                    break

        if tipe == 1:
            temp_origin_list1 = self.adj_list1

            for x in temp_origin_list1:

                if x[0] == origin and x[1] == destination:
                    temp_origin_list1.pop(temp_origin_list1.index(x))
                    break

            for z in temp_origin_list:
                if z[0] == 1 and z[1] == destination:
                    self.adj_list[origin].remove(z)
                    break

            for zz in temp_destination_list:
                if zz[0] == 1 and zz[1] == origin:
                    self.adj_list[destination].remove(zz)
                    break

        if tipe == 2:
            temp_adjlis2 = self.adj_list2
            for aa in temp_adjlis2:
                if aa[0] == destination:
                    self.adj_list2[origin].remove(aa)
                    break

            for y in temp_origin_list:
                if y[0] == 2 and y[1] == destination:
                    self.adj_list[origin].remove(y)
                    break

    def is_connected(self, origin, destination):
        visited = deque([origin])
        queue = deque([origin])

        while queue:
            s = queue.popleft()
            for x in self.adj_list0[s]:
                if x[0] not in visited:
                    if x[0] == destination:
                        return 1
                    visited.append(x[0])
                    queue.append(x[0])

        return 0

    def min_path(self, origin, destination):
        distance = {origin: 0}
        queue = deque([origin])

        while queue:
            u = queue.popleft()
            d = distance[u] + 1
            for i in self.adj_list0[u]:
                if i[0] not in distance:
                    if i[0] == destination:
                        return d
                    distance[i[0]] = d
                    queue.append(i[0])
        return -1

    def count_city(self, origin, distance):
        open_list = {origin}
        closed_list = set([])

        distances = {origin: 0}

        parents = {origin: origin}
        totalcity = 0

        while len(open_list) > 0:
            current = None

            for v in open_list:
                if current is None or distances[v] + 1 < distances[current] + 1:
                    current = v

            for m, weight in self.adj_list0[current]:

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = current
                    distances[m] = distances[current] + weight
                else:
                    if distances[m] > distances[current] + weight:
                        distances[m] = distances[current] + weight
                        parents[m] = current

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            if distances[current] >= distance:
                break

            open_list.remove(current)
            closed_list.add(current)
        for i in distances:
            if distances[i] <= distance:
                totalcity += 1

        return totalcity

    def count_connected(self):
        unvisited = set(range(len(self.adj_list0)))
        queue = deque()

        count = 0
        while len(unvisited) > 0:
            count += 1
            v = next(iter(unvisited))
            unvisited.remove(v)
            queue.append(v)
            while len(queue) > 0:
                v = queue.popleft()
                for w in self.adj_list0[v]:
                    if w[0] in unvisited:
                        unvisited.remove(w[0])
                        queue.append(w[0])

        return count

    def shortest_path_0(self, origin, destination):
        # A* SEARCH ALGORITHM
        open_list = {origin}
        closed_list = set([])

        distances = {origin: 0}

        parents = {origin: origin}

        while len(open_list) > 0:
            current = None

            for v in open_list:
                if current is None or distances[v] + 1 < distances[current] + 1:
                    current = v

            for m, weight in self.adj_list0[current]:

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = current
                    distances[m] = distances[current] + weight
                else:
                    if distances[m] > distances[current] + weight:
                        distances[m] = distances[current] + weight
                        parents[m] = current

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            if current == destination:
                return distances[destination]

            open_list.remove(current)
            closed_list.add(current)

        return -1

    def shortest_path_1(self, origin, destination):
        # A* SEARCH ALGORITHM
        lanjut = True
        open_list_ori_dest = {origin}
        closed_list_ori_dest = set([])

        distances_ori_dest = {origin: 0}

        parents = {origin: origin}

        while len(open_list_ori_dest) > 0:
            current_ori_dest = None

            for v in open_list_ori_dest:
                if current_ori_dest is None or distances_ori_dest[v] + 1 < distances_ori_dest[current_ori_dest] + 1:
                    current_ori_dest = v

            for m, weight_ori_dest in self.adj_list0[current_ori_dest]:

                if m not in open_list_ori_dest and m not in closed_list_ori_dest:
                    open_list_ori_dest.add(m)
                    parents[m] = current_ori_dest
                    distances_ori_dest[m] = distances_ori_dest[current_ori_dest] + weight_ori_dest
                else:
                    if distances_ori_dest[m] > distances_ori_dest[current_ori_dest] + weight_ori_dest:
                        distances_ori_dest[m] = distances_ori_dest[current_ori_dest] + weight_ori_dest
                        parents[m] = current_ori_dest

                        if m in closed_list_ori_dest:
                            closed_list_ori_dest.remove(m)
                            open_list_ori_dest.add(m)

            open_list_ori_dest.remove(current_ori_dest)
            closed_list_ori_dest.add(current_ori_dest)

        # A* SEARCH ALGORITHM

        open_list_dest_ori = {destination}
        closed_list_dest_ori = set([])

        distances_dest_ori = {destination: 0}

        parents_dest_ori = {destination: destination}

        while len(open_list_dest_ori) > 0:
            current_dest_ori = None

            for v in open_list_dest_ori:
                if current_dest_ori is None or distances_dest_ori[v] + 1 < distances_dest_ori[current_dest_ori] + 1:
                    current_dest_ori = v

            for m, weight in self.adj_list0[current_dest_ori]:

                if m not in open_list_dest_ori and m not in closed_list_dest_ori:
                    open_list_dest_ori.add(m)
                    parents_dest_ori[m] = current_dest_ori
                    distances_dest_ori[m] = distances_dest_ori[current_dest_ori] + weight
                else:
                    if distances_dest_ori[m] > distances_dest_ori[current_dest_ori] + weight:
                        distances_dest_ori[m] = distances_dest_ori[current_dest_ori] + weight
                        parents_dest_ori[m] = current_dest_ori

                        if m in closed_list_dest_ori:
                            closed_list_dest_ori.remove(m)
                            open_list_dest_ori.add(m)

            open_list_dest_ori.remove(current_dest_ori)
            closed_list_dest_ori.add(current_dest_ori)

        if destination in distances_ori_dest:
            r = distances_ori_dest[destination]
        else:
            r = 9999999999

        for f in self.adj_list1:
            if f[0] in distances_ori_dest:
                idx0 = distances_ori_dest[f[0]]
            else:
                idx0 = 9999999999
            if f[1] in distances_dest_ori:
                idx1 = distances_dest_ori[f[1]]
            else:
                idx1 = 9999999999
            if f[2] in distances_ori_dest:
                idx2 = distances_ori_dest[f[2]]
            else:
                idx2 = 9999999999
            if f[3] in distances_dest_ori:
                idx3 = distances_dest_ori[f[3]]
            else:
                idx3 = 9999999999

            dj0 = min(idx0 + idx1, idx2 + idx3)
            r = min(dj0, r)

        if r >= 9999999999:
            return -1
        else:
            # poor variable name
            return r

    def simulate_walk(self, origin, distance):
        now = origin
        walk = 0
        visited = [origin]

        while walk != distance:
            for i in self.adj_list2[now]:
                if len(i) == 0:
                    return now
                if i[0] == origin:
                    return visited[distance % (len(visited))]
                walk += 1
                visited.append(i[0])
                now = i[0]
        return now


inPut = stdin.readline().split()
graph = Graph(int(inPut[0]))

for i in range(int(inPut[1])):
    QUERY = stdin.readline().split()
    if QUERY[0] == 'INSERT':
        if QUERY[1] == '0':
            graph.add_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]), int(QUERY[4]))
        elif QUERY[1] == '1':
            graph.add_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]))
        elif QUERY[1] == '2':
            graph.add_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]))
    if QUERY[0] == 'DELETE':
        graph.delete_edge(int(QUERY[1]), int(QUERY[2]), int(QUERY[3]))
    if QUERY[0] == 'SHORTEST_PATH':
        if QUERY[1] == '0':
            print(graph.shortest_path_0(int(QUERY[2]), int(QUERY[3])))
        if QUERY[1] == '1':
            print(graph.shortest_path_1(int(QUERY[2]), int(QUERY[3])))
    if QUERY[0] == 'IS_CONNECTED':
        print(graph.is_connected(int(QUERY[1]), int(QUERY[2])))
    if QUERY[0] == 'MIN_PATH':
        print(graph.min_path(int(QUERY[1]), int(QUERY[2])))
    if QUERY[0] == 'COUNT_CITY':
        print(graph.count_city(int(QUERY[1]), int(QUERY[2])))
    if QUERY[0] == 'COUNT_CONNECTED':
        print(graph.count_connected())
    if QUERY[0] == 'SIMULATE_WALK':
        print(graph.simulate_walk(int(QUERY[1]), int(QUERY[2])))


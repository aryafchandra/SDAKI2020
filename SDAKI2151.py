# Author : Arya Fakhruddin Chandra
# NPM    : 2006607526
# Adapted from lecture slides
# Score : 100
from sys import stdin


class BinaryHeap:
    def __init__(self):
        self.data = list()

    def parentOf(self, i):
        return (i - 1) // 2

    def leftChildOf(self, i):
        return 2 * i + 1

    def rightChildOf(self, i):
        return 2 * (i + 1)

    def peek(self):
        # findMin
        return self.data[0]

    def size(self):
        return len(self.data)

    def add(self, value):
        self.data.append(value)
        self.percolateUp(len(self.data) - 1)

    def remove(self):
        minVal = self.peek()
        self.data[0] = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        if len(self.data) > 1:
            self.pushDownRoot(0)
        return minVal

    def percolateUp(self, leaf):
        parent = self.parentOf(leaf)
        value = self.data[leaf]
        while (leaf > 0) and (value < self.data[parent]):
            self.data[leaf] = self.data[parent]
            leaf = parent
            parent = self.parentOf(leaf)
        self.data[leaf] = value

    def pushDownRoot(self, root):
        heapSize = len(self.data)
        value = self.data[root]
        while root < heapSize:
            childpos = self.leftChildOf(root)
            if childpos < heapSize:
                # choose the smallest child
                if (self.rightChildOf(root) < heapSize) and (self.data[childpos + 1] < self.data[childpos]):
                    childpos += 1
                if self.data[childpos] < value:
                    self.data[root] = self.data[childpos]
                    root = childpos  # keep moving down
                else:  # found right location
                    self.data[root] = value
                    return
            else:  # at a leaf! insert and halt
                self.data[root] = value
                return


binHeap = BinaryHeap()
counter = 0
uang = 0
jumlahVisit = int(stdin.readline())

N = stdin.readline().split()
N1 = stdin.readline().split()

for i in range(jumlahVisit):
    if int(N[i]) == 0:
        binHeap.add(int(N1[i]))
    if int(N[i]) == 1:
        uang = int(N1[i])
        while uang > 0 and binHeap.size() > 0:
            transaksi = binHeap.peek()
            if uang - transaksi >= 0:
                binHeap.remove()
                uang -= transaksi
                counter += 1
            else:
                break

print(counter)

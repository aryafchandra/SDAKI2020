from sys import stdin


# Template given by Pak Surya and from slides
# ini yang pak ustad

class BinaryNode:
    def __init__(self, element=None, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        # TODO: complete this method
        self.root = self.inRec(x, self.root)

    def inRec(self, x, t):
        if t is None:
            t = BinaryNode(x)
        elif x < t.element:
            t.left = self.inRec(x, t.left)
        elif x > t.element:
            t.right = self.inRec(x, t.right)
        else:
            raise Exception('Duplication')
        return t

    def remove(self, x):
        # TODO: complete this method
        self.root = self.remRec(x, self.root)

    def remRec(self, x, t):
        if t is None:
            raise Exception('Not in tree')
        if x < t.element:
            t.left = self.remRec(x, t.left)
        elif x > t.element:
            t.right = self.remRec(x, t.right)
        elif t.left and t.right:
            t.element = self.findMin(t.right).element
            t.right = self.removeMin(t.right)
        else:
            if t.left is not None:
                t = t.left
            else:
                t = t.right
        return t

    def findMin(self, t):
        # TODO: complete this method to support remove
        while t.left:
            t = t.left
        return t

    def removeMin(self, t):
        # TODO: complete this method to support remove
        if t.left:
            t.left = self.removeMin(t.left)
            return t
        else:
            return t.right


def height(t):
    # TODO: complete this method
    if t is None:
        return -1
    else:
        return max(height(t.left) + 1, height(t.right) + 1)


def main():
    N = int(next(stdin))
    for i in range(N):
        # reading P and the distances
        input = next(stdin).split()
        P = int(input[0])

        # just put each distance in a BST
        b = BinarySearchTree()
        for j in range(1, P + 1):
            b.insert(int(input[P + 1 - j]))  # this method is incomplete

        # reading M
        M = int(next(stdin))
        for j in range(M):
            # reading the distance to be removed
            input = next(stdin).split()
            b.remove(int(input[1]))  # this method is incomplete

        print(height(b.root))  # this method is imcomplete


main()

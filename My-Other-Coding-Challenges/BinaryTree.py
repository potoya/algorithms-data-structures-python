class Node:
    def __init__(self, key, l, r):
        self.key = key
        self.leftChild = l
        self.rightChild = r

    def getDepth(self):
        if self.leftChild == None and self.rightChild == None:
            return 0
        else:
            depthLeft = 0
            if self.leftChild != None:
                depthLeft = 1 + self.leftChild.getDepth()

            depthRight = 0
            if self.rightChild != None:
                depthRight = 1 + self.rightChild.getDepth()

            return max(depthLeft, depthRight)

    #Inserts value on the left subtree
    def insertLeft(self, value):
        if self.leftChild == None:
            self.leftChild = Node(value, None, None)
        elif self.rightChild == None:
            self.rightChild = Node(value, None, None)
        else:
            # Try to insert it first in the left branch
            self.leftChild.insertLeft(value)

    #Inserts right
    def insertRight(self, value):
        if self.leftChild == None:
            self.leftChild = Node(value, None, None)
        elif self.rightChild == None:
            self.rightChild = Node(value, None, None)
        else:
            # Try to insert it first in the left branch
            self.rightChild.insertLeft(value)

    #Inorder traversal
    def traverseInOrder(self, arr):
        if self.leftChild != None:
            self.leftChild.traverseInOrder(arr)
        arr.append(self.key)
        if self.rightChild != None:
            self.rightChild.traverseInOrder(arr)

    #Checks if tree is a binary search tree
    def isBST(self):
        # Base cases
        if self.leftChild == None and self.rightChild == None:
            return True
        elif self.leftChild != None and self.leftChild.key > self.key:
            return False
        elif self.rightChild != None and self.key > self.rightChild.key:
            return False
        else:
            leftSubtreeIsBst = True
            if self.leftChild != None:
                leftSubtreeIsBst = self.leftChild.isBST()
            
            rightSubtreeIsBst = True
            if self.rightChild != None:
                rightSubtreeIsBst = self.rightChild.isBST()

            return leftSubtreeIsBst and rightSubtreeIsBst        
            

# Node class end

####################################################
# Script
####################################################
def buildTestTree():
    root = Node(5, None, None)
    root.insertLeft(2)
    root.insertLeft(10)
    root.insertLeft(1)
    root.insertLeft(4)
    return root

if __name__ == '__main__':
    tree = buildTestTree()
    a = []
    tree.traverseInOrder(a)
    print(a, tree.isBST())

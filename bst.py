#Nautishay Cain
#Lab 6
class Node:
    def __init__(self, value):
        self.left = self.right = None
        self.key = value

class BinarySearchTree:
    def __init__(self):
        self.root = None


def insert(treeRoot, currNode): #(tree(array), node)

    y = None #pointer to store parent node
    x = treeRoot #current node

    while x != None:
        y = x

        if currNode.key < x.key:
            x = x.left
        else:
            x = x.right

        parent = y

        if y == None:
            self.root = currNode
        elif currNode.key < y.key:
            y.left = currNode
        else:
            y.right = currNode
    return treeRoot

def inorder(x):
    if x != None:
        inorder(x.left)
        print(x.key)
        inorder(x.right)

def search(self, k):
    if x == null or k == x.key:
        return x
    if k < x.key:
        return search(x.left, k)
    else:
        return search(x.right, k)

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print(r)

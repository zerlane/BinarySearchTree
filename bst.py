#Nautishay Cain
#Lab 6

import csv
import time
import sys

class Node:
    """Constructing a node. A node can
    have a parent, left child,
    and right child."""
    def __init__(self, data):
        self.left = self.right = self.parent = None
        self.key = data

def insert(root, key):
    new_node = Node(key) #creates a new Node of the element being inserted
    x = root #root node
    y = None #trailing pointer (previous pointer of current Node)

    while x != None: #run loop until null pointer is reached
        y = x

        if key < x.key:
            x = x.left
        else:
            x = x.right

    if y == None:
        y = new_node
    elif key < y.key:
        y.left = new_node
    else:
        y.right = new_node

    return y

sys.setrecursionlimit(600000)
def inorder(x):
    if x != None:
        inorder(x.left)
        print(x.key)
        inorder(x.right)

def search(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x

#read in CSV file


if __name__ == '__main__':

    csv_file = "/Users/zerlane/Documents/UAB Summer22/CS303/Labs/Lab6/UPC.csv"
    data_file = "/Users/zerlane/Documents/UAB Summer22/CS303/Labs/Lab6/input.dat"

    with open(data_file, 'r+') as file:
        reader = csv.reader(file)

        items = list(reader)
        upc_codes = [] #builds the BST faster

        for i in range(0, len(items)):
            value = int(items[i][0])
            upc_codes.append(value)

        root = None
        root = insert(None, int(items[0][0]))
        for j in range(1, len(upc_codes)):
            insert(root, upc_codes[j])

        print("Inorder Transversal: ")
        inorder(root)

        #print description of searched upc code
        def getDescription(root, value):
            inTree = search(root, value)

            if inTree:
                for x in range(0,len(items)):
                    try:
                        pos = items[x].index(str(value))
                        return x
                        break
                    except:
                        pass
            else:
                print("This product does not exist.")

        start = time.time()
        searched_description = getDescription(root, 123)
        end = time.time()

        print("")
        print(f"It took {end - start} seconds to search for element corresponding with the UPC code: 123")
        print(f"Description: {items[searched_description][2]}")

    file.close()

    #Test Driver Code
    # root = None
    # root = insert(root, 48)
    # insert(root, 32)
    # insert(root, 18)
    # insert(root, 55)
    # insert(root, 72)
    # insert(root, 58)


    # inorder traversal of the BST
    # inorder(root)

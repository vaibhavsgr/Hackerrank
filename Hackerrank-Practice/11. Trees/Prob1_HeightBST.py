class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
    # this is a node of the tree , which contains info as data, left , right
'''
def height(info):
    #return log(n+1, 2)
    if info != None:
        return _height(info, 0)
    else: return 0

def _height(cur_node, cur_height):
    if cur_node == None:
        return cur_height-1
    left_height = _height(cur_node.left, cur_height+1)
    right_height = _height(cur_node.right, cur_height+1)
    return max(left_height, right_height)


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])

print(height(tree.root))

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
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    #Enter your code here
    if self.root != None:
        return _lca(root, v1, v2)
    else: return 0

def _lca(root, v1, v2):
    # If both n1 and n2 are smaller than root, then LCA lies in left
    if v1 < root && v2 < root:
        return _lca(cur_node.left, v1, v2)

    # If both n1 and n2 are greater than root, then LCA lies in right



tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
v = list(map(int, input().split()))
ans = lca(tree.root, v[0], v[1])
print (ans.info)

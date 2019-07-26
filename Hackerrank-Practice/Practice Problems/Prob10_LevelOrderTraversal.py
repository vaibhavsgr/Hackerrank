class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, n):
        self.q.append(n)

    def dequeue(self):
        return self.q.pop(0)

    def is_empty(self):
        return self.q==[]

class binSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print ("element already in tree")

    def print_tree(self):
        if self.root != None:
            #self._print_tree(self.root)
            self._print_tree_lot(self.root)

    def _print_tree(self, cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print (cur_node.value)
            self._print_tree(cur_node.right_child)


    def _print_tree_lot(self, cur_node):
        Q = Queue()
        Q.enqueue(self.root)

        if cur_node != None:
            while (not Q.is_empty()):
                v = Q.dequeue()
                print (v.value)
                if v.left_child != None:
                    Q.enqueue(v.left_child)
                elif v.right_child != None:
                    Q.enqueue(v.right_child)



tree = binSearchTree()
#tree = fill_tree(tree)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

tree.print_tree()

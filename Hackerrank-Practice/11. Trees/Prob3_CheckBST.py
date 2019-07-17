def checkBST(root, mind=None, maxd= None):
    if root == None:
        return True
    elif mind != None and mind.data >= root.data:
        return False
    elif maxd != None and maxd.data <= root.data:
        return False
    return checkBST(root.left, mind, root) and checkBST(root.right, root, maxd)

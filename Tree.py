class Tree:
    def __init__(self,root,left=None,right=None):
        self.root = root
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.root)

    def total(self):
        if tree==None: return 0
        return total(tree.right)+total(tree.left)+tree.root





tree1 = Tree(2)
tree2 = Tree(3)

print (tree1)

tree3 = Tree(1,tree1,tree2)

print (tree3.total())

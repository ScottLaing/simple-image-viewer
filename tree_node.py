
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build_sample_tree1():
        tn = TreeNode(1)
        tn.left = TreeNode(2)
        tn.right = TreeNode(3)

        tn.left.left = TreeNode(4)
        tn.left.right = TreeNode(5)

        tn.right.left = TreeNode(6)
        tn.right.right = TreeNode(7)

        tn.left.left.left = TreeNode(8)
        tn.left.left.right = TreeNode(9)

        tn.left.right.left = TreeNode(10)
        tn.left.right.right = TreeNode(11)

        tn.right.left.left = TreeNode(12)
        tn.right.left.right = TreeNode(13)

        tn.right.right.left = TreeNode(14)
        tn.right.right.right = TreeNode(15)

        tn2 = TreeNode(1)
        tn2.left = TreeNode(2)
        tn2.right = TreeNode(3)

        tn2.left.left = TreeNode(4)
        tn2.left.right = TreeNode(5)

        tn2.right.left = TreeNode(6)
        tn2.right.right = TreeNode(7)

        tn2.left.left.left = TreeNode(8)
        tn2.left.left.right = TreeNode(9)

        tn2.left.right.left = TreeNode(10)
        tn2.left.right.right = TreeNode(11)

        tn2.right.left.left = TreeNode(12)
        tn2.right.left.right = TreeNode(13)

        tn2.right.right.left = TreeNode(14)
        tn2.right.right.right = TreeNode(15)

        return tn, tn2

    @staticmethod
    def build_sample_tree2():
        tn = TreeNode(3)
        tn.left = TreeNode(9)
        tn.right = TreeNode(20)

        tn.right.left = TreeNode(15)
        tn.right.right = TreeNode(7)

        return tn

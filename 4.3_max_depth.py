# Return maximum depth of a tree (Binary)
# pehle node ko define karo
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None: #tree chu khaelee
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    # Sample tree: 1-2,1-3,2-4,2-5,5-6,5-7,6-8,6-9
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.left.right.left.left = TreeNode(8)
    root.left.right.left.right = TreeNode(9)

    print("Maximum Depth of Tree:", maxDepth(root)) 

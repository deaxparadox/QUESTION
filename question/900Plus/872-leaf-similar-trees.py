from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    state = True
    def get_all_leaf_value(self, root: Optional[TreeNode], collect_value: list) -> None:
        if root:
            self.get_all_leaf_value(root=root.left, collect_value=collect_value)
            self.get_all_leaf_value(root=root.right, collect_value=collect_value)
            if (not root.left) and (not root.right):
                collect_value.append(root.val)
            
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1_leaf_value = []
        tree2_leaf_value = []
        self.get_all_leaf_value(root1, collect_value=tree1_leaf_value)
        self.get_all_leaf_value(root2, collect_value=tree2_leaf_value)
        return tree1_leaf_value == tree2_leaf_value
                
def main():
    s: Solution = Solution()
    s.leafSimilar()
    
if __name__ == "__main__":
    main()
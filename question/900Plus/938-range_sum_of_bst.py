from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calculate(self, root: Optional[TreeNode]) -> None:
        if root:
            self.calculate(root.left)
            self.calculate(root.right)
            if root.val >= self.low and root.val <= self.high:
                self.total += root.val
        return
    total: int = 0
    low: int|None = None
    high: int|None = None
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.calculate(root)
        return self.total
        
def main():
    s: Solution = Solution()
    s.rangeSumBST()
    
if __name__ == "__main__":
    main()
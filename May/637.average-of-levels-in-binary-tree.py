#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
from typing import List


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root:TreeNode) -> List[float]:
        return self.bfs_traversal(root)
    
    def bfs_traversal(self,root):
        res=[]
        que=[root]
        while que:
            lc=0
            ls=0.0
            nodeln=len(que)
            for i in range(nodeln):
                cur=que.pop(0)
                ls+=cur.val
                lc+=1
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(ls/lc)
        return res

# @lc code=end

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s=Solution()
print(s.averageOfLevels(root))


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        res=[]
        que=[root]
        
        while que:
            l_s=0
            l_c=0
            l_size=len(que)
            for i in range(l_size):
                curr=que.pop(0)
                l_s+=curr.val
                l_c+=1
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            res.append(l_s/l_c)
        return res
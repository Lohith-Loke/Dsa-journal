class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_to_tree(preorder):
    stack = []
    for val in preorder:
        node = TreeNode(val)
        if val is None:
            while stack[-1].right is not None:
                stack.pop()
            stack[-1].right = node
        else:
            if stack:
                stack[-1].left = node
            stack.append(node)
    return stack[0]

def bfs_traversal(root):
    if not root:
        return []

    queue = [root]
    result = []

    while queue:
        curr = queue.pop(0)
        result.append(curr.val)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return result


null=None
root = [3,9,20,null,null,15,7]
g=preorder_to_tree(root)
print(bfs_traversal(g))
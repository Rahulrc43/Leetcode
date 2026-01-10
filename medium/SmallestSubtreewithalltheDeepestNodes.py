class Solution:
    def subtreeWithAllDeepest(obj, root):
        def dfs(node):
            if not node:
                return None, 0
            left_root, left_depth = dfs(node.left)
            right_root, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_root, left_depth + 1
            elif right_depth > left_depth:
                return right_root, right_depth + 1
            else:
                return node, left_depth + 1
        answer, _ = dfs(root)
        return answer
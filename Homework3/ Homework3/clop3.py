class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [(root, 0)]
        help_s = []
        ptr = root

        while stack:
            cur_point, length = stack.pop()

            if cur_point.left == None and cur_point.right == None:
                help_s.append(length + 1)

            if cur_point.left != None:
                stack.append((cur_point.left, length + 1))

            if cur_point.right != None:
                stack.append((cur_point.right, length + 1))

        answer = [0] * max(help_s)
        stack = [(root, 0)]
        count = [0] * max(help_s)
        ptr = root

        while stack:
            cur_point, length = stack.pop()

            answer[
                length] += cur_point.val
            count[length] += 1

            if cur_point.left != None:
                stack.append((cur_point.left, length + 1))

            if cur_point.right != None:
                stack.append((cur_point.right, length + 1))

        for i in range(len(answer)):
            answer[i] = answer[i] / count[i]
        return answer
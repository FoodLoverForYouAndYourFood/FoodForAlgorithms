""" Сложность алгоритма O(n) из-за одного цикла."""


class Solution:
    def isPalindrome(self, head):
        clop = head
        pal = ''
        while clop:
            pal = pal + str(clop.val)
            clop = clop.next
        return pal == pal[::-1]


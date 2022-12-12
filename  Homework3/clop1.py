
""" Сложность алгоритма O(n) из-за одного цикла. Проходим по связанному списку и записываем значения,
после чего возвращаем сравнение с обратной строкой."""


class Solution:
    def isPalindrome(self, head):
        clop = head
        pal = ''
        while clop:
            pal = pal + str(clop.val)
            clop = clop.next
        return pal == pal[::-1]


head = [1, 2, 2, 1]

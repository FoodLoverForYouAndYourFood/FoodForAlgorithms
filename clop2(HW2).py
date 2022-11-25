""" Сложность алгоритма O(n) из-за одного цикла"""

def MAXgEN(n):
    nums = [0] * (n + 1)
    nums[1] = 1
    for i in range(1, len(nums)): #заполняем так же как показано в объяснении
        if 2 <= 2 * i <= n:
            nums[2 * i] = nums[i]
        if 2 <= 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]
    return max(nums) # выводим максимальное


print(MAXgEN(3))
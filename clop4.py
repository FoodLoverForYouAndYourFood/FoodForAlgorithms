#Общая сложность программы - #O(n)
def Clop(num, osn): #создаем функци. add с перменной числа и основания СС
    numbers = '' #создаем переменную строкового типа, куда будем полученное значение
    while num != 0: #проверяем равно ли число нулю O(n)
        numbers = str(num % osn) + numbers #записываем в переменную остаток от деления на основание системы
        num //= osn #делим число на основание системы
    return sum(map(int, list(numbers))) #возвращаем список, преобразованный с помощью map в int

print(clop(34, 6)) #передаем значения в функцию
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.

# 2 2
# 4


def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
numberA = int(input('Введите первое число: '))
numberB = int(input('Введите второе число: '))
print(sum(numberA, numberB))
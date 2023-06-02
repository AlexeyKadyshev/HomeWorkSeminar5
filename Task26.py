# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8

def num_degree(num, degree):
    if degree == 1:
        return num
    else:
        return num * num_degree(num, degree - 1)

print(num_degree(int(input("Введите число: ")), int(input("Введите степень: "))))

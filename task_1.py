# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии. 
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A = int(input('Введите число A -> '))
B = int(input('Введите число B -> '))
def Power(A, B):
    if (B < 1):
        return 1
    return A * Power(A, B - 1)
print(Power(A, B))
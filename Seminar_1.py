# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# print('Введите первое число')
# first_namber = int(input())
# print('Введите второе число')
# second_namber = int(input())
# if first_namber*first_namber == second_namber or second_namber*second_namber == first_namber:
#     print('число является квадратом другого')
# else:
#     print('число не является квадратом другого')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# print('Введите первое число')
# a = int(input())
# print('Введите первое число')
# b = int(input())
# print('Введите первое число')
# c = int(input())
# print('Введите первое число')
# d = int(input())
# print('Введите первое число')
# e = int(input())
# max_num = a
# if a > max_num:
#     max_num = a
# if b > max_num:
#     max_num = b
# if c > max_num:
#     max_num = c
# if d > max_num:
#     max_num = c
# if e > max_num:
#     max_num = e
# print(max_num)    




# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# n = int(input('Введите число:\n'))
# n_reverst = n*-1
# print(n_reverst)
# for num in range(n_reverst, n):
#     n_reverst += 1
#     print(n_reverst)


# 2. Напишите программу, которая будет принимать на вход вещественное число и показывать первую цифру дробной части числа.
n = float(input('Введите вещественное число:\n'))
h = n % 10
print()
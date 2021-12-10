
# является ли число простым
# a = int(input("Чтобы узнать является ли чило простым, введите чило "))
# k = 0

# deliteli = []

# for i in range(1, a+1):
#     if a % i == 0:
#         k += 1
#         deliteli.append(i)

# if k == 2:
#     print("simple")
# else:
#     print("not simple")
#     print(deliteli)


# найти сумму цифр введенного числа
# a = int(input("Enter integer "))

# sum = 0
# while a > 0:
#     sum += a % 10
#     a = a // 10
# print(sum)


# Дан список чисел. Превратить его в список квадратов этих чисел

# sp_1 = [7, 7, 8, 9, 33, 2]
# sp_2 = [i**2 for i in sp_1] # генератор списков!!!
# print(sp_2)

# Вводится строка. Требуется удалить повторяющиеся символы и пробелы
# s = input("Enter smth:\n")
# s_new = ""
# for j in s:
#     if j not in s_new and j !=" ":
#         s_new += j
# print(s_new)

# Вводится строка состоящая из слов, разделенных пробелами. 
# Требуется посчитать количество слов в ней.

# s = input("Enter smth: \n")
# print(len(s.split()))



# посчитать сколько было введено чисел больше 10
# a = int(input("Ente a number: \n"))
# i = 0

# while a != 0:
#     if a > 10:
#         i +=1
#     a = int(input("Ente a number: \n"))
# print("There is " +str(i) + " number more than 10!")

# складывает все положительные числа
# a = int(input("Ente a number: \n"))
# sum = 0

# while a != 0:
#     if a > 0:
#         sum = sum + a
#     a = int(input("Ente a number: \n"))
# print(sum)

# a = int(input())
# q = 0

# for i in range(0, a):
#     a = int(input())
#     if a % 6 == 0 and a % 10 == 4:
#         q +=1 # сколько раз это условия было выполено, 
#               # столько раз запишется q
    
# print(q)

# 


# a = float(input())
# sum = 0
# q = 0

# while a != 0:
#     if a % 2 == 0:
#         sum = sum + a
#     q += 1
#     a = float(input())

# print("Сумма четных чисел " + str(sum))
# print("Количество введенных чисел равно " + str(q))

# a = int(input())
# q = [0] * a
# summ = 0

# for i in range(a):
#     q[i]  = int(input())
#     summ = summ + q[i]

# print(q)
# print(summ)


# a = int(input("Введите целое число: "))
# q = [] * aЯ короче такой шел а потом как пришёл
# b = 0

# while a != 0:
#     q.append(a)
#     a = int(input("Введите целое число: "))

# print(q)
# for i in q:
#     if i > 10:
#         b += 1
        
# print(b)

# st = input("")
# c = "о"
# count = 0

# for i in st:
#     if i == c:
#         count +=1
# print(count)

# import random

# n = int(input())
# chisla = [0]*n

# for i in range(n):
#     chisla[i] = random.randint(1, 100)

# print(chisla)
# print(max(chisla))
# print(min(chisla))



# string n = Console.ReadLine();

# n = input("Введите строку: ")
# print (type(n))
# int()
# str()
# float()

# print(int("2408") + 2)
# print(int(14.99))
# n = int(input("Введите число: "))
# print(f'{n} * 2 = {n * 2}')
# print(str(n) * 2)

# n = float(input("введите дробное число: "))
# print(n * 3)
# print(5 // 2) #Целочисленное деление
# print(5 / 2) #Деление с дробной частью
# print(5 % 2) #Остаток от деления
# # 5 : 2 = 2(ост. 1)

# print(int(5 < 7))
# Boolean(Bool)
# True (1)
# False (0)
# && (and) - коньюнкция (логическое умножение)
# || (or) - дизьюнкция (логическое сложение)
# not - отрицание

n = int(input("Введите число: "))
#     1    *     0    +   1    = 1 ("yes")
if n >= 7 and n <= 9 or n > 10:
    print("yes")
else:
    print("no")
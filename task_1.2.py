numbers = []
for i in range(1, 1000, 2):
    i = i ** 3
    numbers.append(i)
print(numbers)
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
result_1 = 0
for i in range(len(numbers)):
    num = numbers[i]
    intermedia = 0
    while num != 0:
        intermedia += num % 10
        num //= 10
    if intermedia % 7 == 0:
        result_1 += numbers[i]
print('Пункт а: ',result_1)
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
numbers_2 = []
for i in range(len(numbers)):
    numbers_2.append(numbers[i] + 17)
#print(numbers_2)
result_2 = 0
for i in range(len(numbers_2)):
    num = numbers_2[i]
    intermedia = 0
    while num != 0:
        intermedia += num % 10
        num //= 10
    if intermedia % 7 == 0:
        result_2 += numbers_2[i]
print('Пункт b: ',result_2)
# c. * Решить задачу под пунктом b, не создавая новый список.
result_3 = 0
for i in range(len(numbers)):
    num = numbers[i] + 17
    intermedia = 0
    while num != 0:
        intermedia += num % 10
        num //= 10
    if intermedia % 7 == 0:
        result_3 += numbers[i] + 17
print('Пункт c: ',result_3)

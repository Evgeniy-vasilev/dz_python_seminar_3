# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def in_binary(number):
    list = []

    while number != 0:
        list.append(number % 2)
        number //= 2

    return ''.join(str(i) for i in list)[::-1]


number = int(input('Введите число: '))
print(in_binary(number))

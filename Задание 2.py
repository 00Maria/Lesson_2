'''Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить
на своем месте.
Для заполнения списка элементов необходимо использовать
функцию input().'''

list = input('Введите несколько элементов ').split()

for i in range(0, len(list) - 1, 2):
    list[i], list[i + 1] = list[i + 1], list[i]
print(list)

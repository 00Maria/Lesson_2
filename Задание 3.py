'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна,
лето, осень).
Напишите решения через list и через dict.'''
month = int(input('Введите номер месяца '))
list = ['winter', 'spring', 'summer', 'autumn']
dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 12 or month == 1 or month == 2:
    print(list[0])
    print(dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(list[1])
    print(dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(list[2])
    print(dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(list[3])
    print(dict.get(4))
elif month >= 12 or month <= 1:
    print('Номер месяца введен некорректно')

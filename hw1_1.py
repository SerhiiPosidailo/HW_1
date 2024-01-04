# 4) переробити це завдання під меню
print('1.Найти min число в листі')
print('2.Видалити всі однакові значення')
print('3.Замінити кожну четверте(4) значення на "X')
print('4.Вивести середне орифметичне значення')
print('5.Виход')


while True:
    res = input('Enter your number: ')
    ls_1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

    if res == '1':
        print(ls_1)
        print(f'min number', min(ls_1))
    elif res == '2':
        print(ls_1)
        print(list(set(ls_1)))
    elif res == '3':
        for i in range(3, len(ls_1), 4):
            ls_1[i] = 'X'
        print(ls_1)
    elif res == '4':

        print(f'середне значення', sum(ls_1) / len(ls_1) )
    elif res == '5':
        break
    else:
        print('Invalid input')


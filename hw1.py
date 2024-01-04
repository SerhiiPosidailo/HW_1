""" 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі."""

st = 'as 23 fdfdg544'
# st = input('please enter your string: ')

new_st = []

for i in st:
    if i.isdigit():
        new_st += i
print(','.join(new_st))
# -----------------------------------------------------------------------


"""2)написати прогу яка вибирає зі введеної строки числа і виводить їх
так як вони написані
наприклад:
st = 'as 23 fdfdg544 34' #введена строка
23, 544, 34              #вивело в консолі"""

st = 'as 23 fdfdg544 34'
# st = input('please enter your string: ')
new_st = st.split()

res = []
string = ''

for i in new_st:
    if i.isdigit():
        res.append(i)
    else:
        for y in i:
            if y.isdigit():
                string += y
        res.append(string)
        string = ''

if res[0] == '':
    print(', '.join(res[1:]))
else:
    print(', '.join(res))
# -------------------------------------------------------------------

# list comprehension

""" 1)є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']"""

greeting = 'Hello, world'
result = [i for i in greeting.upper()]
print(result)

# print([i for i in greeting.upper()])
# --------------------------------------------------------------


""" 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]"""

result_2 = [i ** 2 for i in range(50) if i % 2 == 1]
print(result_2)


# function-------------------------------------------------


# створити функцію яка виводить ліст
def list_func():
    print(list(), type(list()))


list_func()


# створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_num_func(n1, n2, n3):
    return max(n1, n2, n3)


max_num = (max_num_func(23, -1, 77))
print(max_num)


# створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_max_number(*args):
    print(max(args))
    return min(args)


min_number = min_max_number(23, 4555, 123214, -3, 234, 654)
print(min_number)

# створити функцію яка повертає найбільше число з ліста
ls_1 = [23, 4555, 123214, -3, 234, 654]


def return_max_number(ls):
    return max(ls)


max_num_return = return_max_number(ls_1)
print(max_num_return)


# створити функцію яка повертає найменьше число з ліста

def return_min_number(ls):
    return min(ls)


min_num_return = return_min_number(ls_1)
print(min_num_return)

# створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
ls_2 = [23, 55, 77, 80]


def sum_func(ls):
    return sum(ls)


result_sum = sum_func(ls_2)
print(result_sum)


# створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def arithmetic_mean(ls):
    return sum(ls) / len(ls)


result = arithmetic_mean(ls_2)
print(result)

################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
list2 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
print(min(list2))

#   - видалити усі дублікати
print(list(set(list2)))

#   - замінити кожне 4-те значення на 'X'
for i in range(3, len(list2), 4):
    list2[i] = 'X'

print(list2)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def fun_square(n1, n2):
    print('*' * n1)
    for i in range(n2):
        print(f'* {' ' * (n1 - 4)} *')
    print('*' * n1)


fun_square(10, 10)
# 3) вывести табличку множення за допомогою цикла while

size = 9
row = 1

while row <= size:
    col = 1
    while col <= size:
        result = row * col
        print(f"{result:5}", end="")
        col += 1
    print()
    row += 1

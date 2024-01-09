"""1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи"""
from typing import Callable

# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list.append(todo)
#         return todo_list
#
#     def get_all():
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all
#
# add_case, all_case = notebook()
#
# print(all_case())
# print(add_case('homework'))
# print(all_case())
# print(add_case('hello'))
# print(all_case())


"""2) протипізувати перше завдання"""


def notebook() -> tuple[Callable[[str], list], Callable[[], list]]:
    todo_list: list = []

    def add_todo(todo: str) -> list:
        nonlocal todo_list
        todo_list.append(todo)
        return todo_list

    def get_all() -> list:
        nonlocal todo_list
        return todo_list

    return add_todo, get_all


add_case, all_case = notebook()

"""3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:
expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'"""


def expanded_form(number: int) -> str:
    num_str: str = str(number)
    length: int = len(num_str)

    result: list = []
    for i, d in enumerate(num_str):
        if d != '0':
            result.append(d + '0' * (length - i - 1))
    return ' + '.join(result)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

"""4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
продекорована цим декоратором, та буде виводити це значення після виконання функцій"""


def decor(func):
    count: int = 0

    def inner():
        nonlocal count
        count += 1
        print(f'Count: {count}')
        func()
        print('-' * 10)

    return inner


@decor
def func1() -> None:
    print('func1')


@decor
def func2() -> None:
    print('func2')


func1()
func1()
func1()
func2()
func2()
func2()
func2()
func2()
func2()
func2()
func1()
func1()
func1()

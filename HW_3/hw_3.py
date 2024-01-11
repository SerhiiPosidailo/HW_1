from abc import ABC
from typing import List

"""Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін"""


class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x * self.y + other.x * other.y

    def __sub__(self, other):
        return self.x * self.y - other.x * other.y

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y

    def __ne__(self, other):
        return self.x * self.y != other.x * other.y

    def __lt__(self, other):
        return self.x * self.y < other.x * other.y

    def __gt__(self, other):
        return self.x * self.y > other.x * other.y

    def __len__(self):
        return self.x + self.y


r1 = Rectangle(5, 5)
r2 = Rectangle(1, 2)

print(r1 + r2)
print(r1 - r2)
print(r1 == r2)
print(r1 != r2)
print(r1 < r2)
print(r1 > r2)
print(len(r1))
print(len(r2))

"""створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, 
та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення"""


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count += 1

    def __str__(self):
        return str(self.__dict__)


class Prince(Human):
    def __init__(self, name, age, shoe_found):
        super().__init__(name, age)
        self.shoe_found = shoe_found

    def find_shoe(self, cinderellas: List[Cinderella]):
        for cinderella in cinderellas:
            if self.shoe_found == cinderella.shoe_size:
                return cinderella
        return 'Not found'


list_cinderellas = [
    Cinderella('Diana', 19, 36),
    Cinderella('Vika', 22, 28),
    Cinderella('Tanya', 28, 34),
    Cinderella('Sveta', 18, 35)
]

prince = Prince('Serj', 30, 28)

print(prince.find_shoe(list_cinderellas))
print(Cinderella.count)


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
class Printable(ABC):
    def __init__(self):
        pass

    def print_1(*args, **kwargs):
        pass

    def __str__(self):
        return str()

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable


class Book(Printable):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Magazine(Printable):
    def __init__(self, name):
        super().__init__()
        self.name = name


""" 3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають
 є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу"""


class Main(Printable):
    printable_list = []

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, value):
        if isinstance(value, Book) or isinstance(value, Magazine):
            cls.printable_list.append(value)

    @classmethod
    def show_all_magazines(cls):
        for magazine in cls.printable_list:
            if isinstance(magazine, Magazine):
                cls.print_1(magazine.name)

    def print_1(*args, **kwargs):
        print(*args, **kwargs)

    @classmethod
    def show_all_books(cls):
        for book in cls.printable_list:
            if isinstance(book, Book):
                cls.print_1(book.name)


Main.add(Magazine('BookStore'))
Main.add(Book('Python'))
Main.add(Magazine('BookStore2'))
Main.add(Magazine('BookStore3'))
Main.add(Book('Against the road to victory'))
Main.add(Book('JavaScript'))

Main.show_all_magazines()
print('-'*40)
Main.show_all_books()

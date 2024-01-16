import json

# 1) Є ось такий файл... ваша задача записати в новий файл тільки
# email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)

try:
    with open('emails.txt', 'r+') as file, open('gmail_file', 'w') as gmail_file:
        for i in file:
            if 'gmail.com' in i:
                gmail_file.write(i[35:])
except Exception as error:
    print(error)


# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

purchase_list = []
try:
    with open('purchase.json', 'w') as purchase_file:
        json.dump(purchase_list, purchase_file)
except Exception as error:
    print(error)


def get_purchase_list():
    try:
        with open('purchase.json') as all_file:
            print('*' * 20)
            print(json.load(all_file))
            print('*' * 20)
    except Exception as err:
        print(err)


def set_purchase():
    purchase_id = input('Enter the purchase id: ')
    purchase_name = input('Enter the purchase name: ')
    purchase_price = float(input('Enter the purchase price: '))

    try:
        purchase = {
            'id': purchase_id,
            'name': purchase_name,
            'price': purchase_price
        }

        with open('purchase.json', 'r') as set_file:
            purchases = json.load(set_file)

        purchases.append(purchase)

        with open('purchase.json', 'w') as set_file:
            json.dump(purchases, set_file)

    except Exception as err:
        print(err)


def purchase_for_value():
    print('1) id\n2) name\n3) price')
    result_input = input('Enter your number value: ')
    value = input('Enter your value: ')

    try:
        found_purchases = []
        with open('purchase.json') as value_file:
            list_purchase = json.load(value_file)
            for purchase in list_purchase:
                if str(purchase[result_input]) == value:
                    found_purchases.append(purchase)

        for item in found_purchases:
            print('*' * 20)
            print(f'id:{item['id']}, name:{item['name']}, price:{item['price']}')
            print('*' * 20)

    except Exception as e:
        print(e)


def most_expensive_purchase():
    try:
        with open('purchase.json', 'r') as expensive_file:
            all_file = json.load(expensive_file)
            list_file = list(all_file)
            list_file.sort(key=lambda x: x['price'], reverse=True)
            print('*'*20)
            print(list_file[0])
            print('*' * 20)
    except Exception as e:
        print(e)


def del_by_id():
    try:
        with open('purchase.json', 'r+') as del_file:
            del_file_by_id = input('Enter the number by which you want to delete the id: ')
            all_file = json.load(del_file)
            shopping_list = [purchase for purchase in all_file if purchase['id'] != del_file_by_id]
            del_file.seek(0)
            json.dump(shopping_list, del_file)
            del_file.truncate()
            print(f'Purchase ID {del_file_by_id} deleted.')
    except Exception as e:
        print(e)


def menu():
    while True:
        print('------Menu------')
        print('1. Remove all purchases')
        print('2. Add purchase')
        print('3. Search for a purchase')
        print('4. Remove the most expensive purchase')
        print('5. Delete purchase by ID')
        print('9. Go out')
        value_input = input('Select an option: ')

        if value_input == '1':
            get_purchase_list()
        elif value_input == '2':
            set_purchase()
        elif value_input == '3':
            purchase_for_value()
        elif value_input == '4':
            most_expensive_purchase()
        elif value_input == '5':
            del_by_id()
        elif value_input == '9':
            print('Goodbye')
            break


menu()

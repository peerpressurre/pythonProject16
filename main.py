import csv
try:
    begin = input('Ви маєте акаунт?(y/n)')
    datafile = 'data.csv'
    if begin == 'n':
        def signup():
            print('Створення акаунту')
            loginc = input('Придумайте логін - ')
            passwordc = input('Придумайте пароль - ')
            path = input('Введіть шлях ->')
            csv_columns = [loginc, passwordc, path]

            try:
                with open(datafile, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
            except IOError:
                print('I/P error')
        signup()

    if begin == 'y':
        print('Вхід в акаунт')
        counter = 0
        while counter < 4:
            loginw = input('Логін - ')
            passwordw = input('Пароль - ')
            if loginw in datafile:
                if passwordw in datafile:
                    print('Вхід успішний!')
                    with open(datafile, 'r') as csvfile:
                        write = csvfile.readline().split(',')
                    print(bool(loginw == write[0]))
                else:
                    print('Невірний пароль. Спробуйте знову')
            else:
                print('Невірний логін. Спробуйте знову')
            counter += 1
        print('Максимальна кількість спроб вичерпана. Спробуйте пізніше.')

    product = input('Введіть назву продукту - ')
    category = input('Введіть назву категорії - ')
    amount = input('Введіть кількість - ')
    description = input('Введіть опис - ')
    price = input('Введіть ціну товара - ')
    store = input('Введіть магазин купівлі - ')
    csv_columns1 = ['Продукт', 'Категорія', 'Кількість', 'Опис', 'Ціна', 'Магазин']

    dict_data = [
        {'Продукт': product, 'Категорія': category, 'Кількість': amount,
            'Опис': description, 'Ціна': price, 'Магазин': store}
    ]

    csv_file = "manager.csv"

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns1)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    if loginw != write[0]:
        print('Невірний логін')
    if passwordw != write[1]:
        print('Невірний пароль')

    else:
        print('Перевірте ввод символів!')
except Exception as e:
    print(e)
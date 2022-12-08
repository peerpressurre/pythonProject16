import csv
try:
    begin = input('Ви маєте акаунт?(y/n)')
    if begin == 'n':
        print('Створення акаунту')
        loginc = input('Придумайте логін - ')
        passwordc = input('Придумайте пароль - ')
        path = input('Введіть шлях ->')
        signup = [
            {'login': loginc, 'password': passwordc, 'path': path}
        ]
        csv_columns = ['login', 'password', 'path']
        datafile = 'logindata.csv'

        try:
            with open(datafile, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns)
                writer.writeheader()
                for data in signup:
                    writer.writerow(data)
        except IOError:
            print('I/P error')
        print('Реєстрація пройшла успішно')

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

        csv_file = loginc + '_data.csv'

        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns1)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)

            with open(csv_file, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row[0], '-----', row[1], '-----', row[2], '-----', row[3], '-----', row[4], '-----', row[5])
        except IOError:
            print("I/O error")


    if begin == 'y':
        print('Вхід в акаунт')
        counter = 0
        while counter < 4:
            loginw = input('Логін - ')
            passwordw = input('Пароль - ')
            datafile = loginw + '.csv'
            print(datafile)
            print([0])
            print(datafile[1])
            print(datafile[4])
            print(datafile[5])



            if loginw == datafile[0]:
                if passwordw == datafile[1]:
                    print('Вхід успішний!')

                    csv_file = loginw + '_data.csv'
                    with open(csv_file, "r", newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            print(row[0], '-----', row[1], '-----', row[2], '-----', row[3], '-----', row[4], '-----',
                                  row[5])
                else:
                    print('Невірний пароль. Спробуйте знову')
                    counter += 1
            else:
                print('Невірний логін. Спробуйте знову')
                counter += 1
        print('Максимальна кількість спроб вичерпана. Спробуйте пізніше.')
        breakpoint()

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

        with open(csv_file, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], '-----', row[1], '-----', row[2], '-----', row[3], '-----', row[4], '-----', row[5])
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
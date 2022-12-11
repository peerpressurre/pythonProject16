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
        datafile = loginc + '.csv'

        try:
            with open(datafile, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns)
                writer.writeheader()
                for data in signup:
                    writer.writerow(data)
        except IOError:
            print('I/P error')
        print('Реєстрація пройшла успішно')

        # with open(datafile, 'r') as csvfile:
        #     write = csvfile.readline().replace('\n', '').split(',')
        #
        # print(write)

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

            read = []
            with open(csv_file, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    for index in range(0, len(row)):
                        read.append(row[index])

            for i in read:
                i.split(';')
                print(i)



        except IOError:
            print("I/O error")

    if begin == 'y':
        print('Вхід в акаунт')
        counter = 0
        while counter < 4:
            loginw = input('Логін - ')
            passwordw = input('Пароль - ')
            datafile = loginw + '.csv'
            with open(datafile, 'r') as csvfile:
                write = csvfile.readline().replace('\n', '').split(',')

            print(write)

            if loginw == write[0]:
                if passwordw == write[1]:
                    print('Вхід успішний!')

                    print('Оберіть дію:\nПрочитати дані - r\nДодати інформацію - a\nПереписати файл - w')
                    action = input('->')

                    if action == 'r':
                        csv_file = loginw + '_data.csv'
                        with open(csv_file, "r", newline="") as file:
                            reader = csv.reader(file)
                            # проблема з індексами
                            for row in reader:
                                for index in range(0, len(row)):
                                    read.append(row[index])

                        for i in read:
                            i.split(';')
                            print(i)

                    if action == 'a':
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
                        try:

                            with open(datafile, 'a') as csvfile:
                                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns)
                                writer.writeheader()
                                for data in signup:
                                    writer.writerow(data)
                        except IOError:
                            print('I/P error')

                    if action == 'w':

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

                        with open(csv_file, 'w') as csvfile:
                            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns1)
                            writer.writeheader()
                            for data in dict_data:
                                writer.writerow(data)

                else:
                    counter += 1
                    print('Невірний пароль. Спробуйте знову')

            else:
                counter += 1
                print('Невірний логін. Спробуйте знову')

        print('Максимальна кількість спроб вичерпана. Спробуйте пізніше.')
        breakpoint()

except Exception as ex:
    print(ex)


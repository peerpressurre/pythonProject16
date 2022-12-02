import csv
accountfile = 'account.csv'
login = input('enter your login->')
password = input('enter your password->')
path = input('enter path of file->')

data = [
    {'login': login},
    {'password': password},
    {'path': path}
]
columns = ['login', 'password', 'path']
# data_str = f'login: {login},password: {password},path: {path}'
# data_str = data_str.split(',')
# for key in data_str:
#     print(key, end='\n')

with open(accountfile, 'w', newline='') as accountfile:
    writer = csv.DictWriter(accountfile, fieldnames=columns)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

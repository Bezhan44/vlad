import pyshorteners

# Создаём экземпляр класса Shortener
s = pyshorteners.Shortener()
# Пользователь вводит ссылку
url = input('Введите ссылку для сокращения: ')
# Сокращаем ссылку и выводим её
print(s.tinyurl.short(url))
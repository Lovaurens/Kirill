import random as rand

length_of_passwod = int(input('Возраст\n'))
length_of_passwod = int(input('Страна\n'))
length_of_passwod = int(input('Город\n'))
length_of_passwod = int(input('Длина пароля\n'))

password = ''
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
symbols = '1234567890'\
          'ывтапшыщаышвиафыиаоыфволаиытьыфлдасфгкс'\
          '!@#$%^&*()_+-='

for i in range (length_of_passwod):      #'0 - 9'
    symbol = rand.choice(symbols)
    password += symbol

print(password)

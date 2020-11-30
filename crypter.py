#!/usr/bin/env python3
from cryptography.fernet import Fernet
import colorama
from colorama import Fore, Back, Style

colorama.init()

def encrypt(filename, key):
# Зашифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # прочитать все данные файла
        file_data = file.read()
    # Зашифровать данные
    encrypted_data = f.encrypt(file_data)
    # записать зашифрованный файл
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, key):
# Расшифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

print(Fore.CYAN + '''
╔═══╗────────╔╗───────╔╗─╔═══╗
║╔═╗║───────╔╝╚╗─────╔╝║─║╔═╗║
║║─╚╬═╦╗─╔╦═╩╗╔╬══╦═╗╚╗║─║║║║║
║║─╔╣╔╣║─║║╔╗║║║║═╣╔╝─║║─║║║║║
║╚═╝║║║╚═╝║╚╝║╚╣║═╣║─╔╝╚╦╣╚═╝║
╚═══╩╝╚═╗╔╣╔═╩═╩══╩╝─╚══╩╩═══╝
──────╔═╝║║║ Coded by TG @RubySide
──────╚══╝╚╝
Создано для систем linux/termux.
При применении данного скрипта, размер файла не должен превышать объем оперативной памяти.''' + Fore.WHITE)

choose = input('\nВыберите действие: c/d (зашифровать/дешифровать): ')

if choose == 'c':
	file = input('Введите полный путь до шифруемого файла (пример: /sdcard/file.txt): ')
	key = Fernet.generate_key()
	encrypt(file, key)
	print('\nФайл успешно зашифрован с ключом {}{}{}!'.format(Fore.YELLOW, key, Fore.WHITE))
elif choose == 'd':
	file = input('Введите полный путь до дешифруемого файла (пример: /sdcard/file.txt): ')
	key = input('Введите ключ шифрования: ')
	decrypt(file, key)
	print('\n{}Файл успешно расшифрован!{}'.format(Fore.GREEN, Fore.WHITE))
else:
	print('\n{}Ошибка!{}'.format(Fore.RED, Fore.WHITE))
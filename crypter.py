#!/usr/bin/env python3
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()

def crypt(file, password):
	import pyAesCrypt
	bufferSize = 512 * 1024
	pyAesCrypt.encryptFile(str(file), str(file) + ".aes", password, bufferSize)
	os.remove(file)
	print('{}Файл {} успешно зафифрован!{}'.format(Fore.GREEN, file + ".aes", Fore.WHITE))

def decrypt(file, password):
	import pyAesCrypt
	bufferSize = 512 * 1024
	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
	os.remove(file)
	print('{}Файл {} успешно расшифрован!{}'.format(Fore.GREEN, file, Fore.WHITE))

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
	path = input('Введите полный путь до шифруемого файла (пример: /sdcard/file.txt): ')
	key = input('Введите ключ шифрования: ')
	crypt(path, key)
elif choose == 'd':
	path = input('Введите полный путь до дешифруемого файла (пример: /sdcard/file.txt): ')
	key = input('Введите ключ шифрования: ')
	decrypt(path, key)
else:
	print('\n{}Ошибка!{}'.format(Fore.RED, Fore.WHITE))
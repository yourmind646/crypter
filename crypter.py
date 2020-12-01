#!/usr/bin/env python3
try:
	import os
	import colorama
	from colorama import Fore, Back, Style

	colorama.init()

	def crypt(file):
		import pyAesCrypt
		key = input('Введите ключ шифрования\n>>> ')
		bufferSize = 512 * 1024
		pyAesCrypt.encryptFile(str(file), str(file) + ".aes", key, bufferSize)
		os.remove(file)
		print('{}Файл {} успешно зашифрован!{}'.format(Fore.GREEN, file + ".aes", Fore.WHITE))

	def decrypt(file):
		import pyAesCrypt
		key = input('Введите ключ шифрования\n>>> ')
		bufferSize = 512 * 1024
		pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), key, bufferSize)
		os.remove(file)
		print('\n{}Файл {} успешно расшифрован!{}'.format(Fore.GREEN, file, Fore.WHITE))

	print(Fore.CYAN + '''
╔═══╗────────╔╗───────╔╗──╔╗
║╔═╗║───────╔╝╚╗─────╔╝║─╔╝║
║║─╚╬═╦╗─╔╦═╩╗╔╬══╦═╗╚╗║─╚╗║
║║─╔╣╔╣║─║║╔╗║║║║═╣╔╝─║║──║║
║╚═╝║║║╚═╝║╚╝║╚╣║═╣║─╔╝╚╦╦╝╚╗
╚═══╩╝╚═╗╔╣╔═╩═╩══╩╝─╚══╩╩══╝
──────╔═╝║║║ Coded by TG @RubySide
──────╚══╝╚╝
Создано для систем Linux/Termux.''' + Fore.WHITE)

	choose = input('\nВыберите действие: c/d (зашифровать/дешифровать)\n>>> ')

	if choose == 'c':
		path = input('Введите путь до шифруемого файла (пример: /sdcard/file.txt)\n>>> ')
		crypt(path)
	elif choose == 'd':
		path = input('Введите полный путь до дешифруемого файла (пример: /sdcard/file.txt)\n>>> ')
		decrypt(path)
	else:
		print('\n{}Ошибка! Такого действия не существует.{}'.format(Fore.RED, Fore.WHITE))

except EOFError:
	print('\n{}Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except KeyboardInterrupt:
	print('\n\n{}Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except OSError:
	print('\n{}Ошибка! Файл не найден.{}'.format(Fore.RED, Fore.WHITE))
except ValueError:
	print('\n{}Ошибка! Введен неверный ключ или файл не зашифрован.{}'.format(Fore.RED, Fore.WHITE))
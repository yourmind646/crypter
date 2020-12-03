#!/usr/bin/env python3
try:
	import os
	import colorama
	from colorama import Fore, Back, Style
	import pyAesCrypt

	colorama.init()

	class dirNotContainsSlash(Exception):
		pass

	class fileNotCrypted(Exception):
		pass

	class fileAlreadyCrypted(Exception):
		pass

	class fileAlreadyDecrypted(Exception):
		pass

	class selectedActionIsNotExist(Exception):
		pass

	def crypt(path):
		bufferSize = 512 * 1024

		if os.path.isdir(path):
			if path.endswith('/'):
				directory = os.listdir(path)
				directory = filter(lambda x: not x.endswith('.aes'), directory)
				
				key = input('Введите ключ шифрования\n>>> ')
				print()

				for fls in directory:
					pyAesCrypt.encryptFile(str(path + fls), str(path + fls) + ".aes", key, bufferSize)
					os.remove(path + fls)
					print('{}Файл {} успешно зашифрован!{}'.format(Fore.GREEN, (path + fls) + ".aes", Fore.WHITE))
			else:
				raise dirNotContainsSlash()
		else:	
			if not path.endswith('.aes'):
				key = input('Введите ключ шифрования\n>>> ')
				pyAesCrypt.encryptFile(str(path), str(path) + ".aes", key, bufferSize)
				os.remove(path)
				print('\n{}Файл {} успешно зашифрован!{}'.format(Fore.GREEN, path + ".aes", Fore.WHITE))
			else:
				raise fileAlreadyCrypted()
		
	def decrypt(path):
		bufferSize = 512 * 1024

		if os.path.isdir(path):
			if path.endswith('/'):
				directory = os.listdir(path)
				directory = filter(lambda x: x.endswith('.aes'), directory)

				key = input('Введите ключ шифрования\n>>> ')
				print()

				for fls in directory:
					pyAesCrypt.decryptFile(str(path + fls), str(os.path.splitext(path + fls)[0]), key, bufferSize)
					os.remove(path + fls)
					print('{}Файл {} успешно расшифрован!{}'.format(Fore.GREEN, path + fls, Fore.WHITE))
			else:
				raise dirNotContainsSlash()
		else:	
			if path.endswith('.aes'):
				key = input('Введите ключ шифрования\n>>> ')
				pyAesCrypt.decryptFile(str(path), str(os.path.splitext(path)[0]), key, bufferSize)
				os.remove(path)
				print('\n{}Файл {} успешно расшифрован!{}'.format(Fore.GREEN, path, Fore.WHITE))
			else:
				raise fileAlreadyDecrypted()

	print(Fore.MAGENTA + '''
╔═══╗────────╔╗───────╔╗─╔═══╗
║╔═╗║───────╔╝╚╗─────╔╝║─║╔═╗║
║║─╚╬═╦╗─╔╦═╩╗╔╬══╦═╗╚╗║─╚╝╔╝║
║║─╔╣╔╣║─║║╔╗║║║║═╣╔╝─║║─╔═╝╔╝
║╚═╝║║║╚═╝║╚╝║╚╣║═╣║─╔╝╚╦╣║╚═╗
╚═══╩╝╚═╗╔╣╔═╩═╩══╩╝─╚══╩╩═══╝
──────╔═╝║║║ Coded by TG @RubySide
──────╚══╝╚╝
Создано для систем Linux/Termux.''' + Fore.WHITE)

	choose = input('\nВыберите действие: c/d (зашифровать/дешифровать)\n>>> ')

	if choose == 'c':
		files = input('Введите путь до шифруемого файла или каталога (пример: /sdcard/path.txt или dir/)\n>>> ')
		crypt(files)
	elif choose == 'd':
		files = input('Введите полный путь до дешифруемого файла или каталога (пример: /sdcard/path.txt или dir/)\n>>> ')
		decrypt(files)
	else:
		raise selectedActionIsNotExist()	

except EOFError:
	print('\n{}Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except KeyboardInterrupt:
	print('\n\n{}Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except OSError as FileNotFoundError:
	print('\n{}Ошибка! Файл или директория не найден(-а).{}'.format(Fore.RED, Fore.WHITE))
except ValueError:
	print('\n{}Ошибка! Введен неверный ключ.{}'.format(Fore.RED, Fore.WHITE))
except dirNotContainsSlash:
	print('\n{}Ошибка! Каталог должен содержать / на конце.{}'.format(Fore.RED, Fore.WHITE))
except fileAlreadyCrypted:
	print('\n{}Ошибка! Файл уже зашифрован.{}'.format(Fore.RED, Fore.WHITE))
except fileNotCrypted:
	print('\n{}Ошибка! Файл не зашифрован.{}'.format(Fore.RED, Fore.WHITE))
except fileAlreadyDecrypted:
	print('\n{}Ошибка! Файл уже расшифрован.{}'.format(Fore.RED, Fore.WHITE))
except selectedActionIsNotExist:
	print('\n{}Ошибка! Такого действия не существует.{}'.format(Fore.RED, Fore.WHITE))
except Exception:
	print('\n{}Неизвестная ошибка!{}'.format(Fore.RED, Fore.WHITE))

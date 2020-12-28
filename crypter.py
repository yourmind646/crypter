#!/usr/bin/env python3
try:
	import os
	import colorama
	from colorama import Fore, Back, Style
	import pyAesCrypt

	colorama.init()

	mgnt = Fore.MAGENTA
	grn = Fore.GREEN
	rd = Fore.RED
	ylw = Fore.YELLOW
	wht = Fore.WHITE

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
			if not path.endswith('/'):
				path += '/'

			directory = os.listdir(path)
			directory = filter(lambda x: not x.endswith('.aes'), directory)
				
			key = input('Введите ключ шифрования >> ')
			print()

			for fls in directory:
				pyAesCrypt.encryptFile(str(path + fls), str(path + fls) + ".aes", key, bufferSize)
				os.remove(path + fls)
				print('{}[+] Файл {} успешно зашифрован!{}'.format(grn, (path + fls) + ".aes", wht))
		else:	
			if not path.endswith('.aes'):
				key = input('Введите ключ шифрования\n>>> ')
				pyAesCrypt.encryptFile(str(path), str(path) + ".aes", key, bufferSize)
				os.remove(path)
				print('\n{}[+] Файл {} успешно зашифрован!{}'.format(grn, path + ".aes", wht))
			else:
				raise fileAlreadyCrypted()
		
	def decrypt(path):
		bufferSize = 512 * 1024

		if os.path.isdir(path):
			if not path.endswith('/'):
				path += '/'

			directory = os.listdir(path)
			directory = filter(lambda x: x.endswith('.aes'), directory)

			key = input('Введите ключ шифрования >> ')
			print()

			for fls in directory:
				pyAesCrypt.decryptFile(str(path + fls), str(os.path.splitext(path + fls)[0]), key, bufferSize)
				os.remove(path + fls)
				print('{}[+] Файл {} успешно расшифрован!{}'.format(grn, path + fls, wht))
		else:	
			if path.endswith('.aes'):
				key = input('Введите ключ шифрования >> ')
				pyAesCrypt.decryptFile(str(path), str(os.path.splitext(path)[0]), key, bufferSize)
				os.remove(path)
				print('\n{}[+] Файл {} успешно расшифрован!{}'.format(grn, path, wht))
			else:
				raise fileAlreadyDecrypted()

	print(mgnt + '''
   ______                 __           
  / ____/______  ______  / /____  _____
 / /   / ___/ / / / __ \/ __/ _ \/ ___/
/ /___/ /  / /_/ / /_/ / /_/  __/ /    
\____/_/   \__, / .___/\__/\___/_/     
          /____/_/                     
''' 
+ ylw 
+ "\n[*] Версия - 1.3" 
+ "\n[*] Создано для систем Linux/Termux" 
+ "\n[*] Автор скрипта Telegram @RubySide"
+ wht)

	choose = input('\nC/D (зашифровать/дешифровать) >> ')

	if choose == 'c' or choose == 'C':
		files = input('Введите путь >> ')
		crypt(files)
	elif choose == 'd' or choose == 'D':
		files = input('Введите путь >> ')
		decrypt(files)
	else:
		raise selectedActionIsNotExist()	

except EOFError:
	print('\n{}[*] Выход из программы...{}'.format(ylw, wht))
except KeyboardInterrupt:
	print('\n\n{}[*] Выход из программы...{}'.format(ylw, wht))
except OSError as FileNotFoundError:
	print('\n{}[-] Файл или директория не найден(-а).{}'.format(rd, wht))
except ValueError:
	print('\n{}[-] Введен неверный ключ.{}'.format(rd, wht))
except fileAlreadyCrypted:
	print('\n{}[-] Файл уже зашифрован.{}'.format(rd, wht))
except fileNotCrypted:
	print('\n{}[-] Файл не зашифрован.{}'.format(rd, wht))
except fileAlreadyDecrypted:
	print('\n{}[-] Файл уже расшифрован.{}'.format(rd, wht))
except selectedActionIsNotExist:
	print('\n{}[-] Такого действия не существует.{}'.format(rd, wht))
except Exception:
	print('\n{}[-] Неизвестная ошибка!{}'.format(rd, wht))
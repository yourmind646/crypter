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
					print('{}Файл {} успешно зашифрован!{}'.format(grn, (path + fls) + ".aes", wht))
			else:
				raise dirNotContainsSlash()
		else:	
			if not path.endswith('.aes'):
				key = input('Введите ключ шифрования\n>>> ')
				pyAesCrypt.encryptFile(str(path), str(path) + ".aes", key, bufferSize)
				os.remove(path)
				print('\n{}Файл {} успешно зашифрован!{}'.format(grn, path + ".aes", wht))
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
					print('{}Файл {} успешно расшифрован!{}'.format(grn, path + fls, wht))
			else:
				raise dirNotContainsSlash()
		else:	
			if path.endswith('.aes'):
				key = input('Введите ключ шифрования\n>>> ')
				pyAesCrypt.decryptFile(str(path), str(os.path.splitext(path)[0]), key, bufferSize)
				os.remove(path)
				print('\n{}Файл {} успешно расшифрован!{}'.format(grn, path, wht))
			else:
				raise fileAlreadyDecrypted()

	print(mgnt + '''
                                                                     
  .g8"""bgd                                  mm                      
.dP'     `M                                  MM                      
dM'       ` `7Mb,od8 `7M'   `MF'`7MMpdMAo. mmMMmm   .gP"Ya  `7Mb,od8 
MM            MM' "'   VA   ,V    MM   `Wb   MM    ,M'   Yb   MM' "' 
MM.           MM        VA ,V     MM    M8   MM    8M""""""   MM     
`Mb.     ,'   MM         VVV      MM   ,AP   MM    YM.    ,   MM     
  `"bmmmd'  .JMML.       ,V       MMbmmd'    `Mbmo  `Mbmmd' .JMML.   
                        ,V        MM                                 
                     OOb"       .JMML.                            

Версия 1.2.2
Создано для систем Linux/Termux
Автор скрипта TG @RubySide''' + wht)

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
	print('\n{}Выход из программы...{}'.format(ylw, wht))
except KeyboardInterrupt:
	print('\n\n{}Выход из программы...{}'.format(ylw, wht))
except OSError as FileNotFoundError:
	print('\n{}Ошибка! Файл или директория не найден(-а).{}'.format(rd, wht))
except ValueError:
	print('\n{}Ошибка! Введен неверный ключ.{}'.format(rd, wht))
except dirNotContainsSlash:
	print('\n{}Ошибка! Каталог должен содержать / на конце.{}'.format(rd, wht))
except fileAlreadyCrypted:
	print('\n{}Ошибка! Файл уже зашифрован.{}'.format(rd, wht))
except fileNotCrypted:
	print('\n{}Ошибка! Файл не зашифрован.{}'.format(rd, wht))
except fileAlreadyDecrypted:
	print('\n{}Ошибка! Файл уже расшифрован.{}'.format(rd, wht))
except selectedActionIsNotExist:
	print('\n{}Ошибка! Такого действия не существует.{}'.format(rd, wht))
except Exception:
	print('\n{}Неизвестная ошибка!{}'.format(rd, wht))

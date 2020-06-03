from time import sleep
from getpass import getpass
from os import system
system('clear')
while True:
	system('clear')

	print(' _       _________ _        _______ ')
	print("| \    /\\__   __/( (    /|(  ____ \\")
	print('|  \  / /   ) (   |  \  ( || (    \/')
	print('|  (_/ /    | |   |   \ | || |      ')
	print('|   _ (     | |   | (\ \) || | ____ ')
	print('|  ( \ \    | |   | | \   || | \_  )')
	print('|  /  \ \___) (___| )  \  || (___) |')
	print('|_/    \/\_______/|/    )_)(_______)')

	print('‹'+'—'*20+'(Hacking kro Pyaar ni)'+'—'*20+'›')
	user=input('Username:~# ')
	paswd=getpass('Password:~#' )
	if user == 'king' and paswd == 'k41f3140':
		system('clear')
		break
	else:
		print('Invalid user')
		sleep(3)

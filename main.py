# Imports
from comands import Cleaners as clnrs
from comands import Rooms as r


def main():
	game_cycle = True

	while game_cycle:
		clnrs.clean_windows_screen()

		hellouser = r.main_menu()

		if hellouser == 1:
			print("Let's Start!")
		else:
			print("Goodbye!")
			break


if __name__ == '__main__':
	main()
else:
	print("This code is so ass")

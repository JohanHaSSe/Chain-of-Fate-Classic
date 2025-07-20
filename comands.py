# Imports
import os
import time

class Actions():
	def build_table(content: list, lines: int, rows: int):
		'''Universal table builder'''
		tsymb = ["═", "╔", "╦", "╗", "╠", "╬", "╣", "╚", "╩", "╝", "║"]
		
		# Maximum symbols per every row
		line = max(len(x) for x in content)
		

class Rooms():
	"""Co"""

	def main_menu():
		"""Function to the load (in progress) or to start a new game (don't have rn)"""
		game_logo = '''   █████████           ███████████
  ███░░░░░███         ░░███░░░░░░█
 ███     ░░░   ██████  ░███   █ ░ 
░███          ███░░███ ░███████   
░███         ░███ ░███ ░███░░░█   
░░███     ███░███ ░███ ░███  ░    
 ░░█████████ ░░██████  █████      
  ░░░░░░░░░   ░░░░░░  ░░░░░       

'''

		# Rofl
		logo = game_logo.split('\n')
		for line in range(len(logo)):
			print(logo[line], flush=True)
			time.sleep(0.05)

		# Building the table of the choises


		move = int(input("Welcome to this game! Please, select a game or start a new one: "))

		return move

class Cleaners():
	clean_windows_screen = lambda: os.system('cls')  # Clear screen for windows users
	clean_linux_screen = lambda: os.system('clear')  # Clear screen for linux users

#!/usr/bin/env python3

import sys
import difflib
from colorama import Fore, Style
import re

def compare():
	green = Fore.GREEN
	red = Fore.RED
	yellow = Fore.YELLOW 
	reset = Fore.RESET
	 
	original = sys.argv[1]
	compare = sys.argv[2]

	combine_org = []
	combine_comp = []

	for letter in difflib.ndiff(original, compare):
		if letter[0] == "-":
			combine_org.append(f"{red}{letter[2]}")

		elif letter[0] == " ":
			combine_org.append(f"{green}{letter}")

	for letter in difflib.ndiff(original, compare):
		if letter[0] == "+":
			combine_comp.append(f"{red}{letter[2]}")

		elif letter[0] == " ":
			combine_comp.append(f"{green}{letter}")

	show_diff_org = "".join(combine_org).replace(" ","")
	show_diff_comp = "".join(combine_comp).replace(" ","")

	print(f"Original:\t{yellow}{original}\n{reset}Difference:\t{red}{show_diff_org}{reset}")
	#print(f"Second:\t{yellow}{compare} | {reset}Difference: {red}{show_diff_comp}{reset}")


def main():
	if len(sys.argv) < 3:
		print("Missing comparison string!")
		sys.exit(1)

	elif len(sys.argv) > 3:
		print("Too many strings to compare!")
		sys.exit(1)
		
	elif len(sys.argv) == 3:
		compare()

if __name__ == "__main__":
	main()

from termmenu import Menu, EntryNotFoundError
import sys

my_menu = Menu(title="Test!")
my_menu.add_entry("sys.exit(1)", run=lambda: sys.exit(1))
my_menu.add_entry("Print something", run=lambda: print("hello"))
my_menu.add_entry("Do nothing", entry="N")
try:
	result = my_menu.run(allowother=False, message="{entry}) {name}")
except EntryNotFoundError:
	print("That entry doesn't exist")
else:
	print(f"You chose {result}")
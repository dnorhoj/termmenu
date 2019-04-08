import termmenu, sys

my_menu = termmenu.Menu(title="Test!")
my_menu.add_entry("sys.exit(1)", run=lambda: sys.exit(1))
my_menu.add_entry("Print something", run=lambda: print("hello"))
my_menu.add_entry("Do nothing", entry="N")
try:
    result = my_menu.run(allowother=False, message="{}) {}")
except termmenu.EntryNotFoundError:
    print("Oof")
else:
    print(f"You chose {result}") 
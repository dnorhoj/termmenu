from termmenu import Menu, EntryNotFoundError

# Initiate menus
parent_menu = Menu(title="Choose submenu:", start=1)

child_menu_1 = Menu(title="You chose 1!")
child_menu_2 = Menu(title="You chose 2!")
child_menu_3 = Menu(title="You chose 3!")

# Add entries
args = {"allowother":True}

parent_menu.add_entry("Submenu 1", submenu=child_menu_1, submenuargs=args)
parent_menu.add_entry("Submenu 2", submenu=child_menu_2, submenuargs=args)
parent_menu.add_entry("Submenu 3", submenu=child_menu_3, submenuargs=args)

# Run parent_menu
try:
    parent_menu.run()
except EntryNotFoundError:
    print("Please choose a valid menu.")
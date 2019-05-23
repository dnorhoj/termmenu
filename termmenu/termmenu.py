import re

class EntryNotFoundError(Exception): pass

class CustomEntryIsNumberError(Exception): pass

class Menu:
	r"""Create an instance of this class to start off.
	A number of options can be passed to the :class:`Menu` class

	Parameters
	-----------
	title: Optional[:class:`str`]
		This is the text displayed at the top of the menu list.
		Defaults to "Choose one:"
	start: Optional[:class:`int`]
		This changes which number the normal entries indexes from, defaults to 0. :)
	"""


	def __init__(self, **kwargs):
		self.title = kwargs.get('title', 'Choose one:')
		self.start = kwargs.get('start', 0)

		self.entrydict = {}
		self.next = 0
		self.specialentries = {}

	def add_entry(self, text:str, **kwargs):
		r"""This function adds new entries to the list.

		Parameters
		-----------
		text: :class:`str`
			The text next to the number or custom entry key.
		submenu: Optional[:class:`Menu`]
			A Menu that will be ``.run()`` with the arguments specified in the ``submenuargs`` argument.

			If ``submenu`` is specified then the ``run`` argument will not be executed.
		submenuargs: Optional[:class:`dict`]
			Arguments that will be passed to the ``submenu`` when run.
			Example: ``{"allowother": True}``
		run: Optional[:class:`function`]
			Function that will be run when user selects that entry.
			Defaults to ``None`` and it will just return selected entry.
			
			Has lower priority than the ``submenu`` argument
		entry: Optional[:class:`str`]
			Custom entry, instead of number.
			All custom entries will be displayed after the numbered entries.
			Custom entry has to include at least one character that isn't a number or it will raise :class:`CustomEntryIsNumberError`.
			If no entry is specified it will default to using the number after the last number.

		Returns
		--------
		self (:class:`Menu`)
			Returns ``self`` so that you can stack them like
			``Menu().add_entry("1").add_entry("2")``
		"""
		entry = {}
		entry['text'] = text
		run = kwargs.get('run', None)
		submenu = kwargs.get('submenu', None)
		
		entry['submenuargs'] = kwargs.get('submenuargs', {})
		
		if isinstance(submenu, Menu):
			entry['submenu'] = submenu
		else:
			entry['submenu'] = None

		if callable(run) and not entry['submenu'] is None:
			entry['run'] = run
		else:
			entry['run'] = None
		
		customentry = kwargs.get('entry', None)

		if not customentry is None:
			for char in list(customentry):
				if not re.search(r"[0-9]", char):
					self.specialentries[customentry] = entry
					return self

			raise CustomEntryIsNumberError

		self.entrydict[str(self.next+self.start)] = entry
		self.next += 1
		return self

	def run(self, **kwargs):
		r"""This function runs the menu that you have created.

		Parameters
		-----------
		prompt: Optional[:class:`str`]
			The prompt text to be used in the input()
			Defaults to "> "
		allowother: Optional[:class:`bool`]
			Changes wether it's going to return :class:`EntryNotFoundError` if user writes entry that isn't in the list.
			Defaults to ``True``
		listformat: Optional[:class:`str`]
			How the menu list is shown.

			Placeholders
			------------
			{entry}: the number or custom entry.
			{name}: name of the entry.

			Defaults to: "{entry}. {name}" (example: "2. Settings")

		Returns
		--------
		:class:`str`
			Returns the user's input if it doesn't raise EntryNotFoundError.

		"""
		prompt = kwargs.get('prompt', '>')
		listformat = kwargs.get('listformat', "{entry}. {name}")
		allowother = kwargs.get('allowother', False)

		entries = {**self.entrydict, **self.specialentries}

		print(self.title)		
		for name, entry in entries.items():
			print(listformat.format(entry=name, name=entry['text']))

		ans = input(f"{prompt} ")

		for name, entry in entries.items():
			if name.lower() == ans.lower():
				if not entry['submenu'] is None:
					entry['submenu'].run(**entry['submenuargs'])
					return ans

				if not entry['run'] is None:
					entry['run']()
				return ans
		
		if not allowother:
			raise EntryNotFoundError
		
		return ans
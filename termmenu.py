class EntryNotFoundError(Exception):
	pass

class Menu:
	r"""Create an instance of this class to start off.
	A number of options can be passed to the :class:`Menu` class

	Parameters
	-----------
	title: Optional[:class:`str`]
		This is the text displayed at the top of the menu list.
		Defaults to "Choose one:"
	start: Optional[:class:`int`]
		This changes which number the normal entries indexes from, defaults to 1.

	"""


	def __init__(self, **kwargs):
		self.title = kwargs.get('title', 'Choose one:')
		self.start = kwargs.get('start', 1)

		self.entrydict = {}
		self.next = 0
		self.specialentries = {}
	
	def add_entry(self, text:str, **kwargs):
		r"""This function adds new entries to the list.

		Parameters
		-----------
		text: :class:`str`
			The text next to the number or custom entry key.
		run: Optional[:class:`function`]
			Function that will be run when user selects that value.
			Defaults to ``None`` and it will just return selected entry.
		entry: Optional[:class:`str`]
			Todo
		"""
		entry = {}
		entry['text'] = text
		if callable(kwargs.get('run', None)):
			entry['run'] = kwargs.get('run', None)
		
		customentry = kwargs.get('entry', None)

		if not customentry is None:
			self.specialentries[customentry] = entry
			return

		self.entrydict[str(self.next+self.start)] = entry
		self.next += 1

	def run(self, **kwargs):
		prompt = kwargs.get('prompt', '>')
		allowother = kwargs.get('allowother', False)
		message = kwargs.get('message', "{entry}. {name}")

		entries = {**self.entrydict, **self.specialentries}

		print(self.title)		
		for name, entry in entries.items():
			print(message.format(entry=name, name=entry['text']))

		ans = input(f"{prompt} ")

		for name, entry in entries.items():
			if name.lower() == ans.lower():
				if not entry['run'] is None:
					entry['run']()
				return ans
		
		if not allowother:
			raise EntryNotFoundError
		
		return ans
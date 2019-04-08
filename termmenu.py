class EntryNotFoundError(Exception):
	pass

class Menu:
	def __init__(self, **kwargs):
		self.title = kwargs.get('title', 'Choose one:')
		self.start = kwargs.get('start', 1)

		self.entrydict = {}
		self.next = 0
		self.specialentries = {}
	
	def add_entry(self, text:str, **kwargs):
		entry = {}
		entry['text'] = text
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
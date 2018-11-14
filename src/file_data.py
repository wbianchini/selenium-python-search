import json
from pathlib import Path


class FileData:

	def __init__(self):
		self.data = {}
		self.file_name = "input_search.json"

	def get(self):
		"""Get data from given input file and returns it"""
		self.read_from_input_file()
		return self.data
		
	def read_from_input_file(self):
		file = Path(self.file_name)

		with file.open() as read_file:
			self.data = json.load(read_file)

	def set_file_name(self, name):
		"""Set different name for file input"""
		self.file_name = name

	def write_json_to_file(self, data, file_name):
		with open(file_name, 'w') as outfile:
			json.dump(data, outfile)
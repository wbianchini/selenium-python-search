import json
import unittest
from src.file_data import FileData


class FileDataTest(unittest.TestCase):
	
	def setUp(self):
		"""Create new FileData instance"""
		self.file_data = FileData() 

	def test_correct_input_data(self):
		"""Assert given data file have correct key to perform a search"""
		self.file_data.set_file_name("input_search.json")
		data = self.file_data.get()

		self.assertTrue(data["google-me"])

	def test_excepts_if_input_file_does_not_exists(self):
		"""Assert excepts when input file don't exists"""
		self.file_data.set_file_name("test_file.json")
		self.assertRaises(FileNotFoundError, self.file_data.get)


if __name__ == '__main__':
    unittest.main()

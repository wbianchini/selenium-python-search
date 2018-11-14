import os
import os.path
import unittest
from src.google_me import GoogleMe

class GoogleMeTest(unittest.TestCase):

	def setUp(self):
		"""Create new GoogleMe instance"""
		self.googleMe = GoogleMe()

		"""Remove previous output file if exists"""
		if os.path.isfile("output.json"):
			os.remove("output.json")

	def test_google_me(self):
		"""Perform defined search for each given entries"""
		self.googleMe.search()

		"""Assert output index for each term in input term list"""
		output_terms_len = len(self.googleMe.output)
		search_terms_len = len(self.googleMe.file_data.get()["google-me"])
		self.assertEqual(search_terms_len, output_terms_len)

		"""Assert GoogleMe created a output file"""
		self.assertTrue(os.path.isfile("output.json"))

	def tearDown(self):
		"""Close open webdriver session
			and remove tested output file
		"""
		self.googleMe.session.close()
		os.remove("output.json")

if __name__ == "__main__":
	unittest.main()

import unittest
from src.driver import Driver


class DriverTest(unittest.TestCase):

	def setUp(self):
		"""Create new Driver instance"""
		self.sessionWebDriver = Driver()

	def test_environment_has_properly_driver(self):
		"""Assert Driver class were able to properly initiate webdriver."""
		self.assertTrue(self.sessionWebDriver.driver)

	def test_google_page_reachable_and_has_search_input(self):
		driver = self.sessionWebDriver.driver
		"""Navigates to google main page."""
		driver.get("http://www.google.com")

		"""Assert current page has google title."""
		self.assertIn("Google", driver.title)

		"""Assert current page has search input."""
		search_input = driver.find_element_by_name("q")
		self.assertTrue(search_input)

	def tearDown(self):
		"""Close webdriver after all tests execution."""
		self.sessionWebDriver.close_driver()


if __name__ == "__main__":
	unittest.main()

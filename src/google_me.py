from src.driver import Driver
from src.file_data import FileData
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleMe:

	def __init__(self):
		self.output = {}
		self.file_data = FileData()
		
		"""Prepare webdriver with a new session"""
		session_driver = Driver()
		self.session = session_driver.driver

	def search(self):
		"""Perform google search for each input term
			write a output json file with results
		"""
		data = self.file_data.get()

		for term in data["google-me"]:
			self.perform_search(term)

		self.file_data.write_json_to_file(self.output, 'output.json')

	def perform_search(self, term):
		"""Navigate to google main page
			Its more guaranteed if we go back to main page
			on each search.
		"""
		self.session.get("http://google.com")
		search_element = self.session.find_element_by_name("q")
		search_element.send_keys(term)
		search_element.send_keys(Keys.RETURN)

		"""Each google search result is displayed on a div with "g" class"""
		containers = WebDriverWait(self.session, 20).until(
		    EC.presence_of_all_elements_located((By.CLASS_NAME, "g"))
		)

		self.analyze_search_containers(term, containers)

	def analyze_search_containers(self, term, containers):
		""" Get first three term results 
			and store on array under the term index
		"""

		print(term)
		self.output[term] = []

		for container in containers[:3]:
			"""Search titles are displayed on the 
				first h3 element on each search container
			"""
			title = container.find_element_by_css_selector('h3').text
			print(title)
			self.output[term].append(title)


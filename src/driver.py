import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Driver:

	def __init__(self):
		self.set_up_driver()

	def set_up_driver(self):
		"""Initiate a webdriver
			If current environment don't have one 
			it will be set to False as default
		"""
		try:
			self.driver = webdriver.Firefox()
		except Exception:
			self.driver = False

	def close_driver(self):
		"""Close current webdriver session"""
		if not self.driver:
			return;

		self.driver.close()

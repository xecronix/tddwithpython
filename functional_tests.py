#!/usr/bin/env python3

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		
		# Edith wants to check out a new online to-do app
		self.browser.get('http:localhost:8000')

		# She notices the page title mentions to-do lists
		self.assertIn('To-Do', self.browser.title)

		# She's invited to enter a to-do item

		# She enters the to-do item "Buy Peacock fethers" into a textbox

		# When she hits enter, the page updates and now the page lists
		# "1: Buy peacock feathers"

		# there is still a textbox inviting her to enter more items. 

		# She adds a second item "Use peacock fethers to make a fishing fly"

		# The page updates again and now she sees both to-do items.

		# Edith notices instructions for bookmarking a URL where her list can 
		# always be retrieved.

		# She visits the URL to see her list is actually available.

		# Exhausted, she goes to bed.
		self.fail("Finish the test")

if __name__ == '__main__':
	unittest.main()

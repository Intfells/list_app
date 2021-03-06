from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
		
	def test_can_start_a_list_and_retrieve_it_later(self):
#Frances has gradually come to the crushing realisation that she is not happy with her
#working life. She is massively unfulfilled and heads to a cool new site to list some 
#ideas of what she might want to do instead
		self.browser.get('http://localhost:8000')		

#She notices the page-title and header mention to-do lists to start the ball rolling
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
	
#She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)		

#She types 'Buy Peacock Feathers' into a text box as she is a bit of procrastinator (and
#is obsessed with tying fishing lures)
		inputbox.send_keys('Buy peacock feathers')

#When she hits enter, the page updates, and now the page lists
#"1: Buy Peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
#There is still a text-box inviting her to add another item. She enters 'the peacock
#feathers to make a fly" (Frances is very nitpicky)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

#The page updates again and now shows both items on her list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Buy peacock feathers to make a fly')

#She wonders whether the site will remember her list. Then she sees that the site
#has generated a unique url for her...there is some explanatory text to that effect.
		self.fail('Finish the test!')

#She visits that url - her to-do list is still there.

#Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')



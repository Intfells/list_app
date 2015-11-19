from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
#Frances has gradually come to the crushing realisation that she is not happy with her
#working life. She is massively unfulfilled and heads to a cool new site to list some 
#ideas of what she might want to do instead
		self.browser.get('http://localhost:8000')		

#She notices the page-title and header mention to-do lists to start the ball rolling
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

#She is invited to enter a to-do item straight away

#She types 'Buy Peacock Feathers' into a text box as she is a bit of procrastinator (and
#is obsessed with tying fishing lures)

#When she hits enter, the page updates, and now the page lists
#"1: Buy Peacock feathers" as an item in a to-do list

#There is still a text-box inviting her to add another item. She enters 'the peacock
#feathers to make a fly" (Frances is very nitpicky)

#The page updates again and now shows both items on her list
#She wonders whether the site will remember her list. Then she sees that the site
#has generated a unique url for her...there is some explanatory text to that effect.

#She visits that url - her to-do list is still there.

#Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')



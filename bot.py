import sys
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Print things in "one single line"
def print_same_line(text):
  sys.stdout.write('\r')
  sys.stdout.flush()
  sys.stdout.write(text)
  sys.stdout.flush()

# One and only class.
class InstagramBot:
    # Receive password and user.
    def __init__(self, username, password):
      self.username = username
      self.password = password
      # Open chrome web browser.
      self.driver = webdriver.Chrome()
      # Maximize the chrome window.
      # self.driver.maximize_window()

    # Close web browser(Chrome).
    def closeBrowser(self):
      self.driver.close()

    # Login with credentials we set up.
    def login(self):
      driver = self.driver
      # Access instagram website.
      driver.get("https://www.instagram.com/")
      # Take a nap, just to make sure it will load the page.
      time.sleep(1)
      # Seach username field element in HTML.
      user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
      # Nap time.
      time.sleep(1)
      # Input username on field.
      user_name_elem.send_keys(self.username)
      # Search password field element in HTML.
      passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
      # Input password on field.
      passworword_elem.send_keys(self.password)
      # "Press" Enter to send login credentials.
      passworword_elem.send_keys(Keys.RETURN)
      # Nap.
      time.sleep(3)
    
    # Interacting with posts by hashtags.
    def like_photo(self, hashtag):
      driver = self.driver
      driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
      # time.sleep(1)

      # Gathering posts.
      pic_hrefs = []
      for i in range(1, 7):
        try:
          # Scrolling down to load more posts.
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          # Nap time.
          time.sleep(1)
          # Geting elements tags from HTML.
          hrefs_in_view = driver.find_elements_by_tag_name('a')
          # Finding posts hrefs to access later.
          hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
          if '.com/p/' in elem.get_attribute('href')]
          # Building list of unique posts.
          [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
          print_same_line("Check: pic href length " + str(len(pic_hrefs)))
        except Exception:
            # Just move on.
            continue

      # Liking photos
      unique_photos = len(pic_hrefs)
      commentsCount = 0
      for pic_href in pic_hrefs:
        driver.get(pic_href)
        time.sleep(1)

        try:
          like_button = driver.find_elements_by_tag_name("svg")
          for elem in like_button:
            if(elem.get_attribute("aria-label") == "Curtir" and elem.get_attribute("width") == '24'):
              elem.click()
          for second in reversed(range(0, random.randint(5, 11))):
            print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos) + '/ commentsCount:' + str(commentsCount))
          time.sleep(random.randint(2, 13))

          # comment
          randomComments = [ 1,2,3 ]
          randomComments = random.choice(randomComments)
          if(randomComments == 3):
            if(driver.find_element_by_class_name('X7cDz')):
              formArea = driver.find_element_by_class_name('X7cDz')
              formArea.click()
            if(driver.find_element_by_class_name("Ypffh")): 
              commentField = driver.find_element_by_class_name("Ypffh")
              time.sleep(random.randint(2,7))
              comments = ['Приятно','Cool!','Awesome!','Nice!']
              comment = random.choice(comments)
              commentField.send_keys(comment, Keys.ENTER)
              commentsCount += 1
              time.sleep(random.randint(3, 11))
        except Exception as e:
            print("didn't like",e)
            time.sleep(5)
        unique_photos -= 1
    

if __name__ == "__main__":

  # Put your username n your password so the selenium can do the dirty work.
  username = "YOUR_USERNAME"
  password = "YOUR_PASSWORD"

  #  Calls the main function passing user and password to selenium.
  ig = InstagramBot(username, password)
  ig.login()
  # ig.follow_stranges()

  # Random hashtags you can add to like then up.
  hashtags = [ 'like4like', 'skate', 'likeforlike' ]
  
  # Loop of action, 'likes' and 'comments' in this case.
  while True:
    try:
      # Choose a random tag from the list of tags we set up earlier.
      tag = random.choice(hashtags)

      # Calls the function to like and comments posts based on the hashtags we choose up there.
      ig.like_photo(tag)
    except Exception:
      # Close the browser.
      ig.closeBrowser()

      # Wait for 1 minute.
      time.sleep(60)

      # Start all over again after 1 minute.
      ig = InstagramBot(username, password)
      ig.login()
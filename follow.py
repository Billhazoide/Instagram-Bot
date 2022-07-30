from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint


def print_same_line(text):
  sys.stdout.write('\r')
  sys.stdout.flush()
  sys.stdout.write(text)
  sys.stdout.flush()

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(1)
        self.driver.find_element("xpath","//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element("xpath","//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element("xpath",'//button[@type="submit"]')\
            .click()
        # self.driver.get("https://www.instagram.com/" + username + "/")
        
    def get_unfollowers(self):
        sleep(4)
        try:
          sleep(randint(2,4))
          self.driver.get("https://www.instagram.com/" + self.username + "/following")

          following = self._get_names()

          self.driver.get("https://www.instagram.com/" + self.username + "/followers")
          
          followers = self._get_names()

          not_following_me_back = [user for user in following if user not in followers]
          print(not_following_me_back)
        except Exception as e:
          print("Error", e)
        # for user in not_following_me_back:
        #   self.driver.get("https://www.instagram.com/" + user + "/")
         
        #   sleep(1)
        #   # Unfollow option
        #   self.driver.find_element_by_xpath("//span[contains(@aria-label, 'Seguindo')]").click()
          
        #   sleep(randint(1,2))
        #   # Unfollow button
        #   self.driver.find_element_by_xpath("//button[contains(., 'Deixar de seguir')]").click()

        #   sleep(randint(1, 7))

    def _get_names(self):
        # Scrolling list down to get names
        sleep(4)
        try:
          scroll_box = self.driver.find_element(By.CLASS_NAME, value="\\_aano")
          scroll_box.click()
          
          prev_height, height = 0, 1
         
          while prev_height != height:
              prev_height = height
              sleep(randint(2, 3))
              height = self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;", scroll_box)

          # Get element with tag 'a' in scroll_box
          links = scroll_box.find_elements(By.TAG_NAME,'_aacl _aaco _aacw _aacx _aad7 _aade')

          # Get names in "links" element
          names = [name.text for name in links if name.text != '']
          
          
          # Search close button and click
          # close_button = self.driver.find_elements("tag_name","svg")
          # for elem in close_button:
          #   if(elem.get_attribute("aria-label") == "Fechar"):
          #     elem.click()
          return names

        except Exception as e:
          print("Erro", e)
     
my_bot = InstaBot('YOUR_USER', 'YOUR_PASSWORD')
my_bot.get_unfollowers()
from selenium import webdriver  # library
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/Users/aminam/PycharmProjects/Selenium25/chromedriver')
   # Go to the login page
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Entering email
   pytest.driver.find_element_by_id('email').send_keys('ami.morales@gmail.com')
   # Entering password
   pytest.driver.find_element_by_id('pass').send_keys('1234567')
   # Pressing login button
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Checking if we are logged in and main user page is available
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_cnt_pets():
   # Entering email
   pytest.driver.find_element_by_id('email').send_keys('ami.morales@gmail.com')
   # Entering password
   pytest.driver.find_element_by_id('pass').send_keys('1234567')
   # Pressing login button
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Checking if we are logged in and main user page is available
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-deck")))
   # Checking if there are any pets
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr')
   cnt = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
   lines = cnt.split()
   print(lines[2])
   print(len(names))
   assert int(lines[2]) == len(names)


def test_all_pets_with_photo():
   pytest.driver.implicitly_wait(10)
   # Entering email
   pytest.driver.find_element_by_id('email').send_keys('ami.morales@gmail.com')
   # Entering password
   pytest.driver.find_element_by_id('pass').send_keys('1234567')
   # Pressing login button
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Checking if we are logged in and main user page is available
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   # Checking if all pets have photos
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr')
   images = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr th img')
   k=0
   cnt = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
   lines = cnt.split()
   cnt=int(lines[2])
   for i in range(len(names)):
      if images[i].get_attribute('src') != '':
         k+=1
   assert k>=cnt/2


def test_pets_with_alldata():
   pytest.driver.implicitly_wait(10)
   # Entering email
   pytest.driver.find_element_by_id('email').send_keys('ami.morales@gmail.com')
   # Entering password
   pytest.driver.find_element_by_id('pass').send_keys('1234567')
   # Pressing login button
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Checking if we are logged in and main user page is available
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   # Checking if all pets have all data (name, age, type)
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(2)')
   tip = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(3)')
   age = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(4)')
   k=0
   cnt = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
   lines = cnt.split()
   cnt=int(lines[2])
   for i in range(len(names)):
      assert names[i].text != ''
      assert tip[i].text != ''
      assert age[i].text != ''

def test_pets_with_uniquename():
   # Entering email
   pytest.driver.find_element_by_id('email').send_keys('ami.morales@gmail.com')
   # Entering password
   pytest.driver.find_element_by_id('pass').send_keys('1234567')
   # Pressing login button
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Checking if we are logged in and main user page is available
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   # Checking if all pets have uniq names
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(2)')
   x=0
   for i in range(len(names) - 1):
      for j in range(i + 1, len(names)):
         if names[i].text == names[j].text:
            x=1
            quit()
   assert x == 0


def test_all_pets_unique():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('ami.morales@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('1234567')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Checking if there is no pets with the same data
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(2)')
   tip = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(3)')
   age = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(4)')
   uniq = 1
   for i in range(len(names) - 1):
      for j in range(i + 1, len(names)):
         if names[i].text == names[j].text:
            if tip[i].text == tip[j].text:
               if age[i].text == age[j].text:
                  uniq = 0
                  quit()
   assert uniq == 1
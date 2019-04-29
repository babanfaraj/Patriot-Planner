from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Baban Faraj/Documents/College/CS321/project/drivers/chromedriver.exe")
#driver = webdriver.Chrome("project/drivers/chromedriver.exe")

#Test One: Login works
driver.set_page_load_timeout(10)
driver.get("http://127.0.0.1:5000/")
driver.find_element_by_name("email").send_keys("bfaraj@masonlive.gmu.edu")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("login").click()
driver.refresh()

#Test Two: Username and Password invalid
driver.get("http://127.0.0.1:5000/index")
driver.find_element_by_name("email").send_keys("asdf@masonlive.gmu.edu")
driver.find_element_by_name("password").send_keys("adsf")
driver.find_element_by_name("login").click()
time.sleep(1)

#Test Three: Username valid but password invalid
driver.get("http://127.0.0.1:5000/index")
driver.find_element_by_name("email").send_keys("bfaraj@masonlive.gmu.edu")
driver.find_element_by_name("password").send_keys("babaniscool")
driver.find_element_by_name("login").click()
time.sleep(1)

#Test Three: Empty Credentials
driver.get("http://127.0.0.1:5000/index")
driver.find_element_by_name("email").send_keys("")
driver.find_element_by_name("password").send_keys("")
driver.find_element_by_name("login").click()
time.sleep(1)
driver.quit()

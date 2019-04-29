from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Baban Faraj/Documents/College/CS321/project/drivers/chromedriver.exe")
#driver = webdriver.Chrome("project/drivers/chromedriver.exe")

#Login
#driver.set_page_load_timeout(10)
driver.get("http://127.0.0.1:5000/index")
driver.find_element_by_name("email").send_keys("bfaraj@masonlive.gmu.edu")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("login").click()
driver.refresh()

#Test One: Valid password change
driver.get("http://127.0.0.1:5000/settings")
driver.find_element_by_name("new_password").send_keys("password1")
driver.find_element_by_name("confirm_new_password").send_keys("password1")
driver.find_element_by_name("submit").click()
time.sleep(1)

#Test Two: Updating Password with same previous password
driver.get("http://127.0.0.1:5000/settings")
driver.find_element_by_name("new_password").send_keys("password1")
driver.find_element_by_name("confirm_new_password").send_keys("password1")
driver.find_element_by_name("submit").click()
time.sleep(1)


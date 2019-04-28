from selenium import webdriver

driver = webdriver.Chrome()

driver.set_page_load_timeout(10)
driver.get("http://127.0.0.1:5000/")
driver.find_element_by_name("email").send_keys("bfaraj@masonlive.gmu.edu")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("login").click()

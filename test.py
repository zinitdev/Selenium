from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.python.org")

print(driver.title)

driver.close()

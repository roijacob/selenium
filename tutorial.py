import selenium

from selenium import webdriver



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
#driver.close()
#driver.quit()
print(driver.title)
driver.quit()
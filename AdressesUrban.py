from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://cnt-e0583017-61a5-4651-b7d9-0b4b5a3044c3.containerhub.tripleten-services.com/?lng=pt")
time.sleep(2)

driver.find_element(By.ID, "from").send_keys("Comprar um hamster")
time.sleep(1)
driver.find_element(By.ID, "to").send_keys("1300 1st St")
time.sleep(1)
driver.quit()
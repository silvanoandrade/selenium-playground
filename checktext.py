from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# Substitua nosso link pelo link do seu próprio servidor aqui
driver.get("https://cnt-c29f7310-ef0b-4c7f-b701-5f6cad534585.containerhub.tripleten-services.com/?lng=pt")

time.sleep(2)

# Obtém o texto do elemento
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Faça um assert para verificar se o texto da variável disclaimer é "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()
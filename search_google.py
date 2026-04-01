from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_TERM = "Silvano Andrade"

driver = webdriver.Chrome()

try:
    # abre google
    driver.get("https://www.google.com")

    # 🍪 aceita cookies se aparecer
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button/div[contains(text(),'Aceitar') or contains(text(),'Accept all')]")
            )
        )
        cookie_button.click()
    except:
        pass  # se não aparecer, segue normal

    # 🔎 encontra campo de pesquisa
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    # digita a pesquisa
    search_box.send_keys(SEARCH_TERM)

    # pressiona ENTER
    search_box.send_keys(Keys.RETURN)

    # espera resultados aparecerem
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    print("✅ Pesquisa realizada com sucesso!")

finally:
    input("Pressione ENTER para fechar...")
    driver.quit()
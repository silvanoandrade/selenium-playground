import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Dados de exemplo
ADDRESS_FROM = "1300 1st St"
ADDRESS_TO = "East 2nd Street, 601"

# 1️⃣ Abrir o navegador
driver = webdriver.Chrome()

try:
    # 2️⃣ Abrir a página
    driver.get("https://cnt-822e8774-36af-4fa6-8b34-699d66739035.containerhub.tripleten-services.com/?lng=pt")

    # 3️⃣ Esperar o campo "from" estar visível e clicável
    from_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "from"))
    )

    # 4️⃣ Limpar e digitar o endereço de origem
    from_field.clear()
    from_field.send_keys(ADDRESS_FROM)

    # 5️⃣ Esperar o campo "to" estar presente
    to_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "to"))
    )

    # 6️⃣ Limpar e digitar o endereço de destino
    to_field.clear()
    to_field.send_keys(ADDRESS_TO)

    # 7️⃣ Validar se os campos receberam os valores corretos
    assert from_field.get_attribute("value") == ADDRESS_FROM, "O campo FROM não foi preenchido corretamente"
    assert to_field.get_attribute("value") == ADDRESS_TO, "O campo TO não foi preenchido corretamente"

    # 8️⃣ Encontrar o botão "Call Taxi" e verificar se existe
    call_taxi_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(),"Call Taxi")]'))
    )
    assert call_taxi_button is not None, "Botão Call Taxi não encontrado"

    print("✅ Teste concluído com sucesso!")

finally:
    # 9️⃣ Fechar o navegador após 2 segundos
    time.sleep(2)
    driver.quit()
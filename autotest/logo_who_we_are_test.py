from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Создаем экземпляр WebDriver (в данном случае для Chrome)
driver = webdriver.Chrome()

try:
    # Открываем страницу https://welltory.com/plans/
    driver.get("https://welltory.com/plans/")

    # Ожидание загрузки страницы
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ALink_link__cECDm.Header_logoLink__smJHy")))

    # Находим ссылку на логотип и дожидаемся, когда она станет кликабельной
    logo_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".ALink_link__cECDm.Header_logoLink__smJHy"))
    )

    # Получаем URL ссылки на логотип
    logo_link_url = logo_link.get_attribute("href")

    # Проверяем, что URL ссылки на логотип соответствует ожидаемому
    expected_logo_link_url = "https://welltory.com/"
    assert logo_link_url == expected_logo_link_url, f"URL ссылки на логотип не соответствует ожидаемому. Ожидаемый URL: {expected_logo_link_url}, фактический URL: {logo_link_url}"

    # Кликаем по ссылке на логотип
    logo_link.click()

    # Ожидаем, что переход выполнен успешно и мы находимся на странице https://welltory.com/
    WebDriverWait(driver, 15).until(EC.url_to_be("https://welltory.com/"))

    # Проверяем, что на отображаемой странице присутствует текст "A Healthier Happier You"
    expected_text = "A Healthier Happier You"
    assert expected_text in driver.page_source, f"Текст '{expected_text}' не найден на странице"

except (TimeoutException, NoSuchElementException) as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем браузер в любом случае, даже если возникла ошибка
    driver.quit()
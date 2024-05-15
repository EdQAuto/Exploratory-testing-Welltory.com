from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # 1. Открыть страницу https://welltory.com/who-we-are
    driver.get('https://welltory.com/who-we-are')

    # 2. Найти ссылку на логотип
    logo_link = driver.find_element(By.CSS_SELECTOR, 'a.navbar-brand.w-nav-brand')

    # 3. Получить URL ссылки на логотип
    logo_url = logo_link.get_attribute('href').rstrip('/')

    # 4. Проверить, что URL ссылки на логотип соответствует ожидаемому
    expected_logo_url = 'https://welltory.com'
    assert logo_url == expected_logo_url, (
        f"Expected logo URL to be {expected_logo_url}, but got {logo_url}"
    )

    # 5. Кликнуть по ссылке на логотип
    logo_link.click()

    # 6. Проверить, что переход выполнен успешно и мы находимся на странице https://welltory.com/
    WebDriverWait(driver, 10).until(EC.url_to_be('https://welltory.com/'))
    assert driver.current_url.rstrip('/') == 'https://welltory.com', (
        f"Expected URL to be 'https://welltory.com', but got {driver.current_url}"
    )

    # 7. Проверить, что на отображаемой странице присутствует текст "A Healthier Happier You"
    page_text = driver.find_element(By.TAG_NAME, 'body').text
    assert 'A Healthier Happier You' in page_text, (
        "Expected text 'A Healthier Happier You' not found on the page"
    )

finally:
    # 8. Закрыть браузер
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_logo_navigation():
    driver = webdriver.Chrome()
    try:
        driver.get('https://welltory.com/science/')
        logo_link = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.logo.header-logo'))
        )
        logo_url = logo_link.get_attribute('href').rstrip('/')
        expected_logo_url = 'https://welltory.com'
        assert logo_url == expected_logo_url, (
            f"Expected logo URL to be {expected_logo_url}, but got {logo_url}"
        )
        logo_link.click()
        WebDriverWait(driver, 15).until(EC.url_to_be('https://welltory.com/'))
        assert driver.current_url.rstrip('/') == 'https://welltory.com', (
            f"Expected URL to be 'https://welltory.com', but got {driver.current_url}"
        )
        expected_text = "A Healthier Happier You"
        assert expected_text in driver.page_source, f"Текст '{expected_text}' не найден на странице"

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main()

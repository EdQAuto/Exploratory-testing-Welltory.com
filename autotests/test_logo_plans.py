import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_logo_navigation():
    driver = webdriver.Chrome()
    try:
        driver.get("https://welltory.com/plans/")
        WebDriverWait(driver, 15).until(

            EC.presence_of_element_located((By.CSS_SELECTOR, ".ALink_link__cECDm.Header_logoLink__smJHy"))
        )
        logo_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ALink_link__cECDm.Header_logoLink__smJHy"))
        )
        logo_link_url = logo_link.get_attribute("href")
        expected_logo_link_url = "https://welltory.com/"
        assert logo_link_url == expected_logo_link_url, (
            f"URL ссылки на логотип не соответствует ожидаемому. Ожидаемый URL: {expected_logo_link_url}, "
            f"фактический URL: {logo_link_url}"
        )
        logo_link.click()
        WebDriverWait(driver, 15).until(EC.url_to_be("https://welltory.com/"))
        expected_text = "A Healthier Happier You"
        assert expected_text in driver.page_source, f"Текст '{expected_text}' не найден на странице"

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main()

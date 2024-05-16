import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_menu_navigation():
    url = "https://welltory.com/"
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        menu_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="w-dropdown-toggle-0"]'))
        )
        menu_button.click()
        popup_window = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'menu__open-submenu-content'))
        )
        additional_menu_button = WebDriverWait(popup_window, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'menu__submenu-column-title'))
        )
        assert additional_menu_button.is_displayed(), "Кнопка дополнительного меню не отображается"

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Произошла ошибка: {e.__class__.__name__}: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main()

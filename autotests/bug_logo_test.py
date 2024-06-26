import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
    yield driver
    driver.quit()


def test_logo_navigation(browser):
    try:
        # 1. Открываем страницу https://welltory.com/plans/
        browser.get("https://welltory.com/plans/")

        # 2. Находим ссылку на логотип
        logo_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ALink_link__cECDm.Header_logoLink__smJHy'))
        )

        # 3. Получаем URL ссылки на логотип
        logo_url = logo_link.get_attribute('href')

        # 4. Проверяем, что URL ссылки на логотип соответствует ожидаемому
        expected_url = "https://welltory.com/"
        assert logo_url == expected_url, f"URL логотипа {logo_url} не соответствует ожидаемому {expected_url}"

        # 5. Кликаем по ссылке на логотип
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'ALink_link__cECDm.Header_logoLink__smJHy'))
        )
        logo_link.click()

        # Добавляем отладочную информацию
        current_url_after_click = browser.current_url
        print(f"Current URL after click: {current_url_after_click}")

        # 6. Проверяем, что переход выполнен успешно и мы находимся на странице https://welltory.com/
        WebDriverWait(browser, 20).until(EC.url_to_be(expected_url))

        # Повторная проверка текущего URL
        final_url = browser.current_url
        print(f"Final URL after wait: {final_url}")
        assert final_url == expected_url, f"Текущий URL {final_url} не соответствует ожидаемому {expected_url}"

        # 7. Проверяем, что на отображаемой странице присутствует текст "A Healthier Happier You"
        page_text = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'A Healthier Happier You')]"))
        )
        assert page_text is not None, "Текст 'A Healthier Happier You' не найден на странице"

    except TimeoutException as e:
        current_url = browser.current_url
        pytest.fail(f"Test failed due to TimeoutException. Current URL: {current_url}. Exception: {str(e)}")
    except WebDriverException as e:
        pytest.fail(f"Test failed due to WebDriverException: {str(e)}")
    except Exception as e:
        pytest.fail(f"Test failed due to an unexpected exception: {str(e)}")
    finally:
        # 8. Закрываем браузер
        browser.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        logo_link.click()

        # 6. Проверяем, что переход выполнен успешно и мы находимся на странице https://welltory.com/
        WebDriverWait(browser, 10).until(EC.url_to_be(expected_url))
        assert browser.current_url == expected_url, f"Текущий URL {browser.current_url} не соответствует ожидаемому {expected_url}"

        # 7. Проверяем, что на отображаемой странице присутствует текст "A Healthier Happier You"
        page_text = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'A Healthier Happier You')]"))
        )
        assert page_text is not None, "Текст 'A Healthier Happier You' не найден на странице"

    except Exception as e:
        # 8. В случае получения ошибки выводим информацию о деталях ошибки
        pytest.fail(f"Test failed due to: {str(e)}")
    finally:
        # 9. Закрываем браузер
        browser.quit()

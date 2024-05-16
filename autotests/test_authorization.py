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

def test_authorization(browser):
    try:
        # 1. Открываем страницу авторизации
        browser.get("https://app.welltory.com/auth/signin/")

        # 2. Находим поле ввода логина и вводим данные пользователя
        email_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        email_field.send_keys("ilyasoveduard@gmail.com")

        # 3. Находим поле ввода пароля и вводим данные пользователя
        password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        password_field.send_keys("Erik20041984")

        # 4. Находим кнопку "log in" и кликаем по ней
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'Button_button___CNLX.Button_medium__7YPKB.Button_primary__eweQg.AuthForm_button__SAdqO.mb-8.cy-login-button'))
        )
        login_button.click()

        # 5. Проверяем успешную авторизацию (например, по наличию элемента на странице после авторизации)
        account_icon = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'DesktopMenu_email__dlrsx'))  # Обновите селектор на правильный
        )
        assert account_icon is not None, "Авторизация не выполнена успешно."

    except TimeoutException as e:
        current_url = browser.current_url
        pytest.fail(f"Test failed due to TimeoutException. Current URL: {current_url}. Exception: {str(e)}")
    except WebDriverException as e:
        pytest.fail(f"Test failed due to WebDriverException: {str(e)}")
    except Exception as e:
        pytest.fail(f"Test failed due to an unexpected exception: {str(e)}")
    finally:
        # Закрываем браузер
        browser.quit()
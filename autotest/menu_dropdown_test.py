from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск веб-браузера (Chrome) и переход на главную страницу сайта
url = "https://welltory.com/"
driver = webdriver.Chrome()
driver.get(url)

# Находим кнопку меню в шапке лендинга
menu_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//div[@id="w-dropdown-toggle-0"]'))
)

# Нажатие на кнопку меню
menu_button.click()

# Дожидаемся появления всплывающего окна
popup_window = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'menu__open-submenu-content'))
)

# Находим кнопку дополнительного меню в окне
additional_menu_button = WebDriverWait(popup_window, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'menu__submenu-column-title'))
)

# Проверка видимости кнопки дополнительного меню
assert additional_menu_button.is_displayed(), "Кнопка дополнительного меню не отображается"

# Закрываем браузер и завершаем выполнение автотеста
driver.quit()

# A framework for automating testing of website "Welltory" - AI powered copilot for peak wellbeing
<a target="_blank" href="https://www.welltory.com/">welltory.com</a>

![main page screenshot](/pictures/lending.png)

### <a href="https://welltory.com" class="logo header-logo"> <img class="logo__img" src="https://welltory.com/wp-content/themes/Divi-child/img/hrt3.png" alt="logo"></a> О проекте

* Данный проект создается при помощи AI 
* Данный проект осуществляется в рамках исследовательского тестирования
* Данный проект используется как тренажер для практических занятий по автоматизации тестирования

----

### Используемый стэк

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/selenium/selenium-original.svg" title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original.svg" title="PyTest" alt="PyTest" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original.svg" title="PyCharm" alt="PyCharm" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original.svg" title="Git" alt="Git" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/gitlab/gitlab-original.svg" title="GitLab" alt="GitLab" width="40" height="40"/>&nbsp;
  <img title="TestRail" src="pictures/icons/testrail.png" height="40" width="40"/>
  <img src="https://github.com/devicons/devicon/blob/master/icons/jira/jira-original.svg" title="Jira" alt="Jira" width="40" height="40"/>&nbsp;
  <img title="ChatGPT" src="pictures/icons/ChatGPT_logo.svg.png" height="40" width="40"/>
</div>

----

### Список проверок, реализованных в web/UI автотестах

#### 🟢 Авторизация пользователя:

- [x] Успешная аутентификация зарегистрированного ползователя

#### 🟢 Шапка лендинга:

- [x] При нажатии на кнопку <a target="_blank" href="https://welltory.com">Holistic app</a> появляется всплывающее окно с дополнительными кнопками меню
- [x] При нажатии на кнопку <a target="_blank" href="https://welltory.com/who-we-are">Who we are</a> происходит переход на соответствующую страницу сайта
- [x] При нажатии на кнопку <a target="_blank" href="https://welltory.com/science">Science</a> происходит переход на соответствующую страницу сайта
- [x] При нажатии на кнопку <a target="_blank" href="https://welltory.com/plans">Plans</a> происходит переход на соответствующую страницу сайта
      
#### 🟢 Логотип на странице <a target="_blank" href="https://welltory.com/who-we-are">Who we are</a> :

- [x] При нажатии на логотип <img src="https://assets-global.website-files.com/660e8783c2152f6174eadc26/661304852a6aba8cccf8b761_menu%20logo.svg" alt="" width="Auto" class="image-62"> происходит переход на <a target="_blank" href="https://welltory.com">главную</a> страницу сайта

#### 🟢 Логотип на странице <a target="_blank" href="https://welltory.com/science">Science</a> :

- [x] При нажатии на логотип <img src="https://assets-global.website-files.com/660e8783c2152f6174eadc26/661304852a6aba8cccf8b761_menu%20logo.svg" alt="" width="Auto" class="image-62"> происходит переход на <a target="_blank" href="https://welltory.com">главную</a> страницу сайта

#### 🔴 Логотип на странице <a target="_blank" href="https://welltory.com/science">Plans</a> :

- [x] При нажатии на логотип <img src="https://assets-global.website-files.com/660e8783c2152f6174eadc26/661304852a6aba8cccf8b761_menu%20logo.svg" alt="" width="Auto" class="image-62"> происходит переход на <a target="_blank" href="https://welltory.com">главную</a> страницу сайта

#### 🟡 Список проверок, в разработке:

- [ ] Валидация полей формы авторизации
- [ ] Идентификация логина формы авторизации
- [ ] Аутентификация пароля формы авторизации

----

#  🐞❗️❗️❗️БАГ-РЕПОРТ❗️❗️❗️🐞

### Отсутствует переход на главную страницу сайта при клике по логотипу на странице PLANS.

#### Предусловие:

Открыта страница сайта: https://welltory.com/plans/ 

#### Шаги воспроизведения:

Кликнуть по логотипу “Welltory” расположенному в верхнем углу страницы

#### 🟢 Ожидаемый результат: При нажатии на логотип <img src="https://assets-global.website-files.com/660e8783c2152f6174eadc26/661304852a6aba8cccf8b761_menu%20logo.svg" alt="" width="Auto" class="image-62"> происходит переход на главную страницу сайта -  https://welltory.com/ 

#### 🔴 Фактический результат: При нажатии на логотип <img src="https://assets-global.website-files.com/660e8783c2152f6174eadc26/661304852a6aba8cccf8b761_menu%20logo.svg" alt="" width="Auto" class="image-62"> происходит переход на страницу авторизации -  https://welltory.com/auth/signin/ 

#### Окружение Desktop:
1. macOS Sonoma
- браузер Safari, версия 17, разрешение экрана 2560 x 1600
2. Windows 11 Домашняя, версия 21H2,
- браузер Google Chrome, версия 125.0.6422.142, разрешение экрана 1920х1080

https://github.com/EdQAuto/Exploratory-testing-Welltory.com/assets/166423821/ce61ef97-3fd2-4402-81bc-72dd5bf62cd3

#### Окружение Mobile:  iPhone 15 Pro Max, iOS 17.4, браузер Safari 15

https://github.com/EdQAuto/Exploratory-testing-Welltory.com/assets/166423821/2d400277-31b9-4811-b012-e47ab09de582

----

### 🎬 Видео прохождение автотеста с баг репортом

#### 🐞При нажатии на логотип <img src="https://assets-global.website-files.com/660e8783c2152f6174eadc26/661304852a6aba8cccf8b761_menu%20logo.svg" alt="" width="Auto" class="image-62"> на странице <a target="_blank" href="https://welltory.com/plans">Plans</a> , не происходит переход на <a target="_blank" href="https://welltory.com">главную</a> страницу сайта 🐞

https://github.com/EdQAuto/Welltory/assets/166423821/d561a4ee-b8b3-4c84-a36d-43cc66c46f39

## Подробная информация о логах и работе с ChatGPT, содержится в папке: > <a target="_blank" href="https://github.com/EdQAuto/Exploratory-testing-Welltory.com/tree/de1bb04c707ba76ff944cb0e8da36d78d68a3df8/gpt/promt_engineering_tests/">Ссылка</a>
----

# ❗️В РАЗРАБОТКЕ❗️

![main page screenshot](/pictures/mobile.png)

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов в Selenoid
* Запуск mobile автотестов в BrowserStack
* Для запуска mobile автотестов используется Appium

----

### Локальный запуск автотестов

* #### Для запуска web/UI автотестов выполнить в cli:

* #### Для запуска mobile автотестов выполнить в cli:

* #### Для запуска всех автотестов выполнить в cli:

* #### Получение отчёта:

----

### Проект в Jenkins

* #### Параметры сборки:

* #### Запуск автотестов в Jenkins:

----

### Allure отчет

----

### Интеграция с Allure TestOps

----

### Интеграция с Jira

----

### Оповещения в Telegram

----

### Видео прохождения web/UI автотеста

----

### Видео прохождения mobile автотеста


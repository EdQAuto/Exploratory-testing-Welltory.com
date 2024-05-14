# A framework for automating testing of website "Welltory" - AI powered copilot for peak wellbeing
<a href="https://welltory.com" class="logo header-logo"> <img class="logo__img" src="https://welltory.com/wp-content/themes/Divi-child/img/hrt3.png" alt="logo"></a> <a target="_blank" href="https://www.welltory.com/">welltory.com</a>

![main page screenshot](/pictures/start.png)

----

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

### Список проверок, реализованных в web/UI автотестах

#### Главная страница:

- [x] <a target="_blank" href="https://welltory.com">Главная</a> страница сайта отображается
- [x] При нажатии на кнопку 
- [x] При нажатии на кнопку <a target="_blank" href="https://welltory.com/who-we-are">Who we are</a> происходит переход на соответствующую страницу сайта
- [x] При нажатии на кнопку <a target="_blank" href="https://welltory.com/science">Science</a> происходит переход на соответствующую страницу сайта
- [x] При нажатии на кнопку <a target="_blank" href="https://welltory.com/plans">Plans</a> происходит переход на соответствующую страницу сайта
      
#### Логотип на странице <a target="_blank" href="https://welltory.com/who-we-are">Who we are</a> :

- [x] При нажатии на логотип <img src="https://assets-global.website-files.com/660e8783c2152f6174eadc26/661304852a6aba8cccf8b761_menu%20logo.svg" alt="" width="Auto" class="image-62">  происходит переход на <a target="_blank" href="https://welltory.com">главную</a> страницу сайта

#### Логотип на странице <a target="_blank" href="https://welltory.com/science">Science</a> :

- [x] При нажатии на логотип <a href="https://welltory.com" class="logo header-logo"><img class="logo__img" src="https://welltory.com/wp-content/themes/Divi-child/img/hrt3.png" alt="logo"><span class="logo__text"><img src="https://welltory.com/wp-content/themes/Divi-child/img/welltory-logo.svg" alt="welltory-logo"></span></a> происходит переход на <a target="_blank" href="https://welltory.com">главную</a> страницу сайта

#### Логотип на странице <a target="_blank" href="https://welltory.com/science">Plans</a> :

- [x] При нажатии на логотип <a class="ALink_link__cECDm Header_logoLink__smJHy" target="_self" href="/"></a> происходит переход на <a target="_blank" href="https://welltory.com">главную</a> страницу сайта

### Список проверок, реализованных в mobile автотестах

- [x] Элементы управления отображаются
- [x] Раздел "Сериалы" отображается
- [ ] Раздел "Профиль" отображается

----

### Используемый стэк

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original.svg" title="PyTest" alt="PyTest" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original.svg" title="PyCharm" alt="PyCharm" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/selenium/selenium-original.svg" title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;
  <img title="Selenoid" src="pictures/icons/selenoid.png" height="40" width="40"/>
  <img title="Selene" src="pictures/icons/selene.png" height="40" width="40"/>
  <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original.svg" title="Git" alt="Git" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/gitlab/gitlab-original.svg" title="GitLab" alt="GitLab" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/jira/jira-original.svg" title="Jira" alt="Jira" width="40" height="40"/>&nbsp;
  <img title="Allure Report" src="pictures/icons/Allure_Report.png" height="40" width="40"/>
  <img title="Allure TestOps" src="pictures/icons/AllureTestOps.png" height="40" width="40"/>
  <img title="Telegram" src="pictures/icons/tg.png" height="40" width="40"/>
</div>

----

### Локальный запуск автотестов

#### Для запуска web/UI автотестов выполнить в cli:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --browser-version=100 ./tests/web/
```

#### Для запуска mobile автотестов выполнить в cli:
> [!NOTE]
> Ключ `--context` не обязателен, по умолчанию тесты будут запущены на BrowserStack
* Для запуска на реальном устройстве указать ключ `--context=local_real_device`
* Для запуска на виртуальном устройстве указать ключ `--context=local_real_device`
* Для запуска на BrowserStack указать ключ `--context=bstack`

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=bstack ./tests/mobile/
```

#### Для запуска всех автотестов выполнить в cli:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -s -v
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/">Ссылка</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
ENVIRONMENT = ['STAGE', 'PREPROD', 'PROD'] # Окружение
COMMENT = 'some comment' # Комментарий
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/">проект</a>

![jenkins project main page](ivi_ui_and_mobile_test_framework/pictures/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать любое окружение
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

![jenkins_build](ivi_ui_and_mobile_test_framework/pictures/jenkins_build.png)

----

### Allure отчет
#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/">Общие результаты</a>
![allure_report_overview](ivi_ui_and_mobile_test_framework/pictures/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](ivi_ui_and_mobile_test_framework/pictures/allure_reports_suites.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#graph">Графики</a>


![allure_reports_graphs](ivi_ui_and_mobile_test_framework/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](ivi_ui_and_mobile_test_framework/pictures/alluere_reports_graphs_2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3910/dashboards">Ссылка на проект</a>

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/dashboards">Дашборд с общими показателями тестовых прогонов</a>

![allure_test_ops_dashboards](ivi_ui_and_mobile_test_framework/pictures/allure_testops_dashboards.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/launches">История запуска тестовых наборов</a>

![allure_testops_launches](ivi_ui_and_mobile_test_framework/pictures/allure_testops_launches.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Тест кейсы</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_suites.png)

#### <a target="_blank" href="https://allure.autotests.cloud/launch/33573/tree/551292/attachments?treeId=0">Тестовые артефакты</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_test_attachments.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Ручной запуск авто теста из Allure TestOps</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_manual_test_run.png)

1. Нажать на чек-бокс необходимого тест кейса
2. Нажать на "Bulk actions"
3. Нажать на "Run"

----

### Интеграция с Jira
> <a target="_blank" href="https://ed-qa-engineer.atlassian.net/jira/software/projects/KAN/boards/1">Ссылка на проект</a>

![jira_project](ivi_ui_and_mobile_test_framework/pictures/jira_project.png)

----

### Оповещения в Telegram
![telegram_allert](ivi_ui_and_mobile_test_framework/pictures/telegram_allert.png)

----

### Видео прохождения web/UI автотеста
![autotest_gif](ivi_ui_and_mobile_test_framework/pictures/autotest.gif)

----

### Видео прохождения mobile автотеста
![autotest_gif](ivi_ui_and_mobile_test_framework/pictures/test_mobile_video.gif)

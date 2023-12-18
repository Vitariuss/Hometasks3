import logging
from baseApp import BasePage
from selenium.webdriver.common.by import By
import yaml


    #Класс поиск локатора при входе в личный кабинет
class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationHelper(BasePage):

    # Enter text
    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        logging.info(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.debug(f"Exeption while operation with{locator}")
            return False
        return True

    # функция ввода логина

    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_LOGIN"], word, description="login form")

    # функция ввода пароля

    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_PASS"], word, description="pass form")

    # Ввести заголовок нового поста

    def enter_title(self, title):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_POST_TITLE"], title, description="title form")

    # Ввести контент нового поста
    def enter_content(self, content):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], content, description="content form")

    # функция ввода имени в Contact us!
    def enter_contact_name(self, name):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_FIELD_NAME"], name, description="contact form name")

    # функция ввода почты в Contact us!
    def enter_contact_email(self, email):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_FIELD_EMAIL"], email,
                                   description="contact form email")

    # Ввести контент в в Contact us!
    def enter_contact_content(self, content):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_FIELD_CONTENT"], content,
                                   description="contact form content")

    # Click

    def click_button(self, locator, description):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.debug("Exeption with click")
            return False
        logging.info(f"Clicked {element_name} button")
        return True

    # Кликнуть на кнопку настройки
    def clic_btn_setting(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_Setting"], description="button setting")

    # Кликнуть на кнопку профиль
    def clic_btn_profille(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_PROFILE"], description="button profile in setting")

    # Кликнуть на кнопку создать пост
    def clic_btn_new_post(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_NEW_POST"],
                          description="Click button for create new post")

    # функция нажатия кнопки LOGGIN

    def click_btn_log(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_LOG"], description="Click button for login")

    # функция нажатия кнопки отправки в Contact US
    def clic_btn_contactus(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_CONTACT_US"], description="Click button for send contact")

    # Выход из профиля
    def clic_btn_logout(self):
        logging.info("Click button for exit profile")
        self.find_element(TestSearchLocators.ids["LOCATOR_LOGOUT"]).click()

    # Кликнуть на кнопку сохранить пост
    def clic_btn_save_post(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_POST_BTN_SAVE"],
                          description="Click button for create new post")

    # Переход на домашнюю страницу
    def clic_href_home(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HREF_HOME"], description="Click link for go to home page")

    # Переход на страницу Contact us!
    def click_href_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HREF_CONTACT"], description="Click link for go to home page")

    # Get text

    def get_text_from_element(self, locator, description):
        if description:
            element_name = description
        else:
            element_name = locator

        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.debug(f"Exeption while get test from {element_name}")
            return None
        logging.info(f"We find text {text} in field {element_name}")
        return text

    # Функция проверка ошибки
    def get_err_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR"], description="Find error")

    # Найти элемент "Blog"
    def get_txt_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_H1_BLOG"],
                                          description="find element Blog on page")

    # Найти заголовок созданного поста
    def get_txt_title_new_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_H1_TITLE_NEW_POST"],
                                          description="Create new post")

    # Поиск всплывающего сообщения
    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"Get alert text{text}")
        return text
    # # Поиск всплывающего сообщения
    # def get_alert_text(self):
    #     logging.info(f"Get alert text")
    #     text = self.get_alert_text()
    #     logging.info(text)
    #     return text

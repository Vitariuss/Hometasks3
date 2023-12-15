import logging
import time

from baseApp import BasePage
from selenium.webdriver.common.by import By


# Класс поиск локатора при входе в личный кабинет
class TestSearchLocators:
    LOCATOR_LOGIN = (By.XPATH, "/html/body/div/main/div/div/div/form/div[1]/label/input")
    LOCATOR_PASS = (By.XPATH, "/html/body/div/main/div/div/div/form/div[2]/label/input")
    LOCATOR_BTN_LOG = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_H1_BLOG = (By.XPATH, """/html/body/div[1]/main/div/div[1]/h1""")
    LOCATOR_BTN_Setting = (By.XPATH, """/html/body/div[1]/main/nav/ul/li[3]/a""")
    LOCATOR_BTN_PROFILE = (By.XPATH, """/html/body/div[1]/main/nav/ul/li[3]/div/ul/li[1]/span[2]""")
    LOCATOR_BTN_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_POST_TITLE = (
        By.XPATH, """/html/body/div[1]/main/div/div/div[3]/div[2]/div/div[2]/div/form/div/div/div[1]/div/label/input""")
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="update-post-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_POST_BTN_SAVE = (
        By.XPATH, """html/body/div[1]/main/div/div/div[3]/div[2]/div/div[2]/div/form/div/div/div[7]/div/button""")
    LOCATOR_H1_TITLE_NEW_POST = (By.XPATH, """/html/body/div[1]/main/div/div[1]/h1""")
    LOCATOR_HREF_HOME = (By.XPATH, """//*[@id="app"]/main/nav/a""")
    LOCATOR_LOGOUT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/div/ul/li[3]""")
    LOCATOR_HREF_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_FIELD_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_FIELD_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_FIELD_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_BTN_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationHelper(BasePage):

    # функция ввода логина

    def enter_login(self, word):
        logging.info(f"Send{word} to element {TestSearchLocators.LOCATOR_LOGIN[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN)
        login_field.clear()
        login_field.send_keys(word)

    # функция ввода пароля

    def enter_pass(self, word):
        logging.info(f"Send{word} to element {TestSearchLocators.LOCATOR_PASS[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS)
        pass_field.clear()
        pass_field.send_keys(word)

    # функция нажатия кнопки LOGGIN

    def click_btn_log(self):
        logging.info("Click button for login")
        self.find_element(TestSearchLocators.LOCATOR_BTN_LOG).click()

    # функция проверка ошибки

    def get_err_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error {TestSearchLocators.LOCATOR_ERROR[1]}")
        return text

    # Найти элемент "Blog"
    def get_txt_blog(self):
        blog_text = self.find_element(TestSearchLocators.LOCATOR_H1_BLOG, time=3)
        text = blog_text.text
        logging.info(f"We have find text {text} in page {TestSearchLocators.LOCATOR_H1_BLOG[1]}")
        return text

    # Кликнуть на кнопку настройки
    def clic_btn_setting(self):
        logging.info("Click button for open setting")
        self.find_element(TestSearchLocators.LOCATOR_BTN_Setting, time=3).click()

    # Кликнуть на кнопку профиль
    def clic_btn_profille(self):
        logging.info("Click button for open profile")
        self.find_element(TestSearchLocators.LOCATOR_BTN_PROFILE, time=3).click()

    # Кликнуть на кнопку создать пост
    def clic_btn_new_post(self):
        logging.info("Click button for create new post")
        self.find_element(TestSearchLocators.LOCATOR_BTN_NEW_POST, time=10).click()

    # Ввести заголовок нового поста
    def enter_title(self, title):
        logging.info(f"Send{title} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        post_title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        post_title_field.clear()
        post_title_field.send_keys(title)

    # Ввести контент нового поста
    def enter_content(self, content):
        logging.info(f"Send{content} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]},")
        post_content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        post_content_field.clear()
        post_content_field.send_keys(content)

    # Кликнуть на кнопку сохранить пост
    def clic_btn_save_post(self):
        logging.info("Click button for create new post")
        self.find_element(TestSearchLocators.LOCATOR_POST_BTN_SAVE).click()

    # Найти заголовок созданного поста
    def get_txt_title_new_post(self):
        title_new_post_text = self.find_element(TestSearchLocators.LOCATOR_H1_TITLE_NEW_POST, time=2)
        text = title_new_post_text.text
        logging.info(f"We have find text {text} in page {TestSearchLocators.LOCATOR_H1_TITLE_NEW_POST[1]}")
        return text

    # Переход на домашнюю страницу
    def clic_href_home(self):
        logging.info("Click link for go to home page")
        self.find_element(TestSearchLocators.LOCATOR_HREF_HOME).click()

    # Переход на страницу Contact us!
    def click_href_contact(self):
        logging.info("Click link Contact for to go")
        self.find_element(TestSearchLocators.LOCATOR_HREF_CONTACT).click()

    # функция ввода имени в Contact us!
    def enter_contact_name(self, name):
        logging.info(f"Send{name} to element {TestSearchLocators.LOCATOR_FIELD_NAME[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_NAME)
        name_field.send_keys(name)

    # функция ввода почты в Contact us!
    def enter_contact_email(self, email):
        logging.info(f"Send{email} to element {TestSearchLocators.LOCATOR_FIELD_EMAIL[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_EMAIL)
        email_field.send_keys(email)

    # Ввести контент в в Contact us!
    def enter_contact_content(self, content):
        logging.info(f"Send{content} to element {TestSearchLocators.LOCATOR_FIELD_CONTENT[1]},")
        contact_content_text = self.find_element(TestSearchLocators.LOCATOR_FIELD_CONTENT)
        contact_content_text.send_keys(content)

    # функция нажатия кнопки отправки в Contact US
    def clic_btn_contactus(self):
        logging.info("Click button for contact")
        self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT_US).submit()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"Message 'From successfuly submitted'{text}")
        return text

    # Выход из профиля
    def clic_btn_logout(self):
        logging.info("Click button for exit profile")
        self.find_element(TestSearchLocators.LOCATOR_LOGOUT).click()

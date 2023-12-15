import time

from testpage import OperationHelper
import logging
import yaml
import random

russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
exemple_title = ' '.join(random.choices(russian_alphabet, k=7))

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test Start")
    testpage = OperationHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_btn_log()
    assert testpage.get_err_text() == "401"


def test_step_2(browser):
    logging.info("Test Start")
    testpage = OperationHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login(testdata["log"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_btn_log()

    assert testpage.get_txt_blog() == "Blog"
    testpage.clic_btn_setting()
    testpage.clic_btn_logout()

    time.sleep(3)


def test_step_3(browser):
    logging.info("Test Start")
    testpage = OperationHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login(testdata["log"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_btn_log()
    testpage.clic_btn_setting()
    testpage.clic_btn_profille()
    testpage.clic_btn_new_post()
    testpage.enter_title(exemple_title)
    testpage.enter_content("For creating new post we have writing tex in python QA")
    testpage.clic_btn_save_post()

    time.sleep(2)

    assert testpage.get_txt_title_new_post() == exemple_title


    browser.refresh()

    time.sleep(5)

# Обновление страницы браузера


def test_step_4(browser):
    logging.info("Test Start")
    testpage = OperationHelper(browser, testdata["url"])
    testpage.go_to_site()

    testpage.clic_btn_setting()
    testpage.clic_btn_profille()

    testpage.click_href_contact()

    time.sleep(2)

    testpage.enter_contact_name("Duddle")
    testpage.enter_contact_email("Duddle@web.cg")
    testpage.enter_contact_content("Hi! I have a problem")
    testpage.clic_btn_contactus()
    time.sleep(2)
    assert testpage.get_alert_text()

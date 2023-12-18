import time
import pytest
from testpage import OperationHelper
import logging
import yaml
import random
import requests
from conftest import auth_token

russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
exemple_title = ' '.join(random.choices(russian_alphabet, k=7))

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test Start 1")
    testpage = OperationHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_btn_log()
    time.sleep(3)
    assert testpage.get_err_text() == "401"
    time.sleep(3)


# Поиск элемента Blog на странице
def test_step_2(browser):
    logging.info("Test Start 2")
    testpage = OperationHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login(testdata["log"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_btn_log()
    time.sleep(5)
    assert testpage.get_txt_blog() == "Blog"
    testpage.clic_btn_setting()
    testpage.clic_btn_logout()

    time.sleep(3)


# Создание нового сообщения
def test_step_3(browser):
    logging.info("Test Start 3")
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

# Отправка форма контакты
def test_step_4(browser):
    logging.info("Test Start 4")
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
    assert testpage.get_alert_text() == "Form successfully submitted"
    logging.info("Test finished")


def test_step_5(auth_token):
    try:
        logging.info("Test Start 5 API")
        res_get = requests.get(url=testdata['url_post'], headers={"X-Auth-Token": auth_token},
                               params={"owner": "notMe"})
        res_json = res_get.json()
        assert res_get.status_code == 200
        assert 'data' in res_json

        post_titles = [post["title"] for post in res_json["data"]]
        assert testdata["title"] in post_titles

        logging.info("Test 5 finished")
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")

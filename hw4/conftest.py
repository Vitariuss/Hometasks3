import yaml, pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_conf_report import sendemail
import requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="session")
def browser():
    if testdata["browser"] == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

    elif testdata["browser"] == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        yield driver
        driver.quit()
        sendemail()


@pytest.fixture(scope="session")
def auth_token():
    url = testdata["url_login"]
    log = testdata["log"]
    pas = testdata["pass"]
    try:
        response = requests.post(url, data={"username": log, "password": pas})
        response.raise_for_status()
        return response.json()["token"]
    except requests.exceptions.HTTPError as e:
        print(f"An error occurred during authentication request: {e}")
        raise


@pytest.fixture
def post_title(request):
    return request.param


def test_create_post_and_check_description(auth_token):
    url = testdata["url_post"]
    headers = {
        "X-Auth-Token": auth_token
    }
    data = {
        "title": "Создание поста для проверки запросов",
        "description": "Описание нового поста",
        "content": "Содержимое нового поста",
    }

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200, f"The post was created: {response.text}"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    browser.get("http://127.0.0.1:5000")
    yield browser
    browser.quit()


def check_alert(driver, expected):
    alert = WebDriverWait(driver, 5).until(
        EC.alert_is_present()
    )
    assert alert.text == expected
    alert.accept()


def test_empty_username(driver):
    driver.find_element(By.ID, "pwd").send_keys("abc123")
    driver.find_element(By.NAME, "sb").click()
    check_alert(driver, "Username cannot be empty.")


def test_empty_password(driver):
    driver.find_element(By.ID, "username").send_keys("Alice")
    driver.find_element(By.NAME, "sb").click()
    check_alert(driver, "Password cannot be empty.")


def test_short_password(driver):
    driver.find_element(By.ID, "username").send_keys("Alice")
    driver.find_element(By.ID, "pwd").send_keys("abc1")
    driver.find_element(By.NAME, "sb").click()
    check_alert(
        driver,
        "Password must be at least 6 characters long."
    )


def test_valid_input(driver):
    driver.find_element(By.ID, "username").send_keys("Alice")
    driver.find_element(By.ID, "pwd").send_keys("abc123")
    driver.find_element(By.NAME, "sb").click()

    WebDriverWait(driver, 5).until(
        EC.url_contains("/submit")
    )

    assert "Hello, Alice!" in driver.page_source
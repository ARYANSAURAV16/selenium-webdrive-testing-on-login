# test_login.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils import config

def test_login_successful():
    driver = webdriver.Chrome(executable_path="C:\Users\ASUS\PycharmProjects\pythonProject2\testing\drivers\chromedriver.exe")
    driver.get(config.BASE_URL)

    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    login_button = driver.find_element_by_id("login-button")

    username_field.send_keys(config.VALID_USERNAME)
    password_field.send_keys(config.VALID_PASSWORD)
    login_button.click()

    assert "Welcome" in driver.page_source

    driver.quit()

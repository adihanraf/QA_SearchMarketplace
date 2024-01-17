from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import pytest
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

def test_tokped(driver):
    driver.get("https://www.tokopedia.com/")
    search = driver.find_element(By.XPATH, "//input[@type='search']")
    search.send_keys("Helm")
    search.send_keys(Keys.RETURN)
    time.sleep(2)

def test_bukalapak(driver):
    driver.get("https://www.bukalapak.com/")
    search = driver.find_element(By.XPATH, "//input[@id='v-omnisearch__input']")
    search.send_keys("Helm")
    search.send_keys(Keys.RETURN)
    time.sleep(2)


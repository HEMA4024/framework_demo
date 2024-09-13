import pytest
from selenium import webdriver


@pytest.fixture
def driver_init():
    c_options = webdriver.ChromeOptions()
    c_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=c_options)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.close()
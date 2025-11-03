import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import BASE_URL

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    print("🚀 Browser launched")
    driver.get(BASE_URL)
    yield driver
    print("🛑 Quitting browser...")
    driver.quit()

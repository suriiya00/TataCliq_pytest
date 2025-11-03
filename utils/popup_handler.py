from utils.custom_wait import WebDriverWaitCustom
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

def handle_homepage_popup(driver):
    # Wait for popup to load and dismiss if appears
    time.sleep(3)
    try:
        popup_button = WebDriverWaitCustom(driver, 5).until(
            lambda d: d.find_element(By.ID, "moe-dontallow_button"),
            "Popup button not found"
        )
        popup_button.click()
        print("✅ Popup closed by clicking 'Don't Allow'")
    except TimeoutException:
        print("ℹ️ No popup appeared, continuing...")

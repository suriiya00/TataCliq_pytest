import time
import pytest
from utils.custom_wait import WebDriverWaitCustom
from utils.popup_handler import handle_homepage_popup
from page_objects.home_page import HomePage
from page_objects.search_results_page import SearchResultsPage

@pytest.mark.ui
def test_open_homepage(driver):
    print("🏠 Opening homepage")
    handle_homepage_popup(driver)

@pytest.mark.ui
def test_search(driver):
    print("🔍 Searching for 'Watch'")
    search_box = WebDriverWaitCustom(driver, 10).until(
        lambda d: d.find_element(*HomePage.SEARCH_BOX),
        "Search box not found"
    )
    search_box.send_keys("Watch")

    first_suggestion = WebDriverWaitCustom(driver, 5).until(
        lambda d: d.find_element(*HomePage.FIRST_SEARCH_SUGGESTION),
        "Search suggestion not found"
    )
    first_suggestion.click()
    time.sleep(2)

@pytest.mark.ui
def test_apply_filter(driver):
    print("🔧 Applying Women filter")
    women_filter = WebDriverWaitCustom(driver, 10).until(
        lambda d: d.find_element(*SearchResultsPage.WOMEN_FILTER),
        "Women filter not found"
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", women_filter)
    driver.execute_script("arguments[0].click();", women_filter)
    time.sleep(3)

@pytest.mark.ui
def test_open_first_product(driver):
    print("🛒 Opening first product")

    first_product = WebDriverWaitCustom(driver, 10).until(
        lambda d: d.find_element(*SearchResultsPage.FIRST_PRODUCT),
        "First product not found"
    )
    product_name = first_product.text

    driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
    driver.execute_script("arguments[0].click();", first_product)

    WebDriverWaitCustom(driver, 10).until(
        lambda d: len(d.window_handles) > 1,
        "Product page tab did not open"
    )

    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)
    print(f"🔎 Product opened: {product_name}")
    time.sleep(5)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print(f"🔙 Returned to main page after closing '{product_name}' tab")

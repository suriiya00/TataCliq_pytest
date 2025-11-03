from selenium.webdriver.common.by import By

class HomePage:
    SEARCH_BOX = (By.ID, "search-text-input")
    FIRST_SEARCH_SUGGESTION = (By.XPATH, '//*[@id="inside-search-wrapper"]/div[1]/div/div/span[1]')

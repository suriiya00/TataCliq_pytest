from selenium.webdriver.common.by import By

class SearchResultsPage:
    WOMEN_FILTER = (By.XPATH, '//*[@id="l2FilterDiv-1"]/div[2]')
    FIRST_PRODUCT = (By.XPATH, '//*[@id="ProductModule-MP000000026545715"]/a/div')

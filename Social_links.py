from selenium import webdriver
from selenium.webdriver.common.by import By


class Social():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.social_links = []

    def teardown_method(self, method):
        self.driver.quit()

    def social_icon_links(self):
    #checks rediraction of social icon links in footer part -> BUG_2:
    # there are no links in this section. Only icons.
        self.driver.get("http://158.160.56.133/app/pets/")
        self.driver.find_element(By.CSS_SELECTOR, ".instagram").click()
        self.social_links.append(self.driver.current_url)
        self.driver.find_element(By.CSS_SELECTOR, ".tik-tok").click()
        self.social_links.append(self.driver.current_url)
        self.driver.find_element(By.CSS_SELECTOR, ".youtube").click()
        self.social_links.append(self.driver.current_url)
        self.driver.find_element(By.CSS_SELECTOR, ".telegram").click()
        self.social_links.append(self.driver.current_url)
        self.driver.close()
        return self.social_links

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class Header():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.header_links = []
        self.header_responds = []
        self.header_titles = []

    def teardown_method(self):
        self.driver.quit()

    def h_links(self):
# check header links - > all links navigate to the propper pages
        self.driver.get("http://158.160.56.133/app/pets")
        self.driver.find_element(By.LINK_TEXT, "Питомцы").click()
        self.header_links.append(self.driver.current_url)
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "О нас").click()
        self.header_links.append(self.driver.current_url)
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Контакты").click()
        self.header_links.append(self.driver.current_url)
        self.driver.close()

    def h_responses_titles(self):
    # check responeds header links -> all links have 200 status code
        for hlink in self.header_links:
            h_url = str(hlink)
            self.header_responds.append(f"{h_url} - {requests.get(h_url)}")
            response = requests.get(h_url)

    # check titles of header pages -> BUG_1:
    # all pages have the same title
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string
            self.header_titles.append(f"{h_url} - {title}")
            print(self.header_links)
            print(self.header_responds)
            print(self.header_titles)



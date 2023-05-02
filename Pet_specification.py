import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class PetSpecification():
    def __init__(self, driver=None):
        if driver is not None:
            self.driver = webdriver.Firefox()
        self.main_url = "http://158.160.56.133/app/pets"
        self.main_api_url = "http://158.160.56.133/api/"
        self.all_api_links = []
        self.pages = {"page": 1}

        # these 3 lists collect data from api(Classes) and main page (filter section)
        self.api_id_web_species = []
        self.api_name_web_breeds = []
        self.api_code_web_genders = []

    # get values from web page ###################################

    def teardown_method(self, method):
        self.driver.quit()

    def values_from_page(self):
        # get all values from sort fields(species, breed, gender):
        self.driver.get(self.main_url)
        species_list = []
        inline_form_list = ["inline-form-input-species", "inline-form-input-breed", "inline-form-input-gender"]
        for inform in inline_form_list:
            dropdown = self.driver.find_element(By.ID, inform)
            options = dropdown.find_elements(By.TAG_NAME, "option")
            for option in options:
                species_list.append(option.get_attribute("value"))
            species_list.append("next")
        self.driver.quit()
        # put values to the proper lists:
        current_list = self.api_id_web_species
        for items in species_list:
            if items == "next":
                if current_list == self.api_id_web_species:
                    current_list = self.api_name_web_breeds
                elif current_list == self.api_name_web_breeds:
                    current_list = self.api_code_web_genders
                else:
                    break
            else:
                current_list.append(items)

    def print_page_values(self):
        print(self.api_id_web_species, len(self.api_id_web_species))
        print(self.api_name_web_breeds, len(self.api_name_web_breeds))
        print(self.api_code_web_genders, len(self.api_code_web_genders))

    # get values from api ###################################

    def get_all_api_links(self):
        # get all api links to one list
        response = requests.get(self.main_api_url)
        data = json.loads(response.text)
        for item in data:
            if isinstance(data[item], str) and data[item].startswith("http"):
                self.all_api_links.append(data[item])
        return self.all_api_links
        # api_links[0]) pet links[1]) breed links[2]) status links[3]) species links[4]) gender

    def get_api_values_to_list(self, n_link, n_page):
        # number of pages taken from POSTMAN
        current_list = []
        num_link = n_link
        num_page = n_page
        for i in range(1, num_page):
            self.pages["page"] = i
            response = requests.get(self.all_api_links[num_link], params=self.pages)
            current_list += response.json()["results"]
            current_list = sorted(current_list, key=lambda x: x["name"])
        for item in current_list:
            self.api_id_web_species.append(item["id"])
            self.api_name_web_breeds.append(item["name"])
            self.api_code_web_genders.append(item["code"])

    def get_unique_values(self):
        unique_id = list(set(self.api_id_web_species))
        unique_name = list(set(self.api_name_web_breeds))
        unique_code = list(set(self.api_code_web_genders))
        print(f"api id: {len(self.api_id_web_species)} - unique: {len(unique_id)}")
        print(f"api name: {len(self.api_name_web_breeds)} - unique: {len(unique_name)}")
        print(f"api code: {len(self.api_code_web_genders)} - unique: {len(unique_code)}")

    def print_info(self):
        print(self.api_id_web_species)
        print(self.api_name_web_breeds)
        print(self.api_code_web_genders)

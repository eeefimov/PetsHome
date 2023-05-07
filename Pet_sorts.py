from selenium import webdriver
from selenium.webdriver.common.by import By


class Sorting:
    def __init__(self):
        self.driver = webdriver.Firefox()
        #sort lists from page
        self.sort_species = []
        self.sort_breeds = []
        self.sort_genders = []
        self.main_url = "http://158.160.56.133/app/pets"

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
        current_list = self.sort_species
        for items in species_list:
            if items == "next":
                if current_list == self.sort_species:
                    current_list = self.sort_breeds
                elif current_list == self.sort_breeds:
                    current_list = self.sort_genders
                else:
                    break
            else:
                current_list.append(items)



        print(self.sort_species, len(self.sort_species))
        print(self.sort_breeds, len(self.sort_breeds))
        print(self.sort_genders, len(self.sort_genders))



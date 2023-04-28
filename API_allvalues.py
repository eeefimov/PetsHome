import json
import requests


class APIValues():
    def __init__(self, num_link, num_page):
        self.main_api_url = "http://158.160.56.133/api/"
        self.all_api_links = []
        self.all_api_id = []
        self.all_api_name = []
        self.all_api_code = []
        self.num_link = num_link
        self.num_page = num_page
        self.pages = {"page": 1}

    def get_all_api_links(self):
        # get all api links to one list
        response = requests.get(self.main_api_url)
        data = json.loads(response.text)
        for item in data:
            if isinstance(data[item], str) and data[item].startswith("http"):
                self.all_api_links.append(data[item])
        print(self.all_api_links)
        # api_links[0]) pet links[1]) breed links[2]) status links[3]) species links[4]) gender

    def get_api_values_to_list(self):
        # number of pages taken from POSTMAN
        current_list = []
        for i in range(1, self.num_page):
            self.pages["page"] = i
            response = requests.get(self.all_api_links[self.num_link], params=self.pages)
            current_list += response.json()["results"]
            current_list = sorted(current_list, key=lambda x: x["name"])
        for item in current_list:
            self.all_api_id.append(item["id"])
            self.all_api_name.append(item["name"])
            self.all_api_code.append(item["code"])

    def print_info(self):
        print(self.all_api_id)
        print(self.all_api_name)
        print(self.all_api_code)

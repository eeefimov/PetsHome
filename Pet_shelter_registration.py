import json
import requests


class PetShelterRegistration():
    def __init__(self):
        self.reg_url = "http://158.160.56.133/api/pet_shelter_req"
        self.pages = {"page": 1}
        self.reg_id = []
        self.reg_phone_num = []
        self.reg_email = []
        self.reg_firstname = []
        self.reg_middlename = []
        self.reg_lastname = []
        self.reg_comment = []
        self.reg_pet = []

    def post_reg_values(self):
        data = {
            'phone_num': '+79234564321',
            'email': 'asd@asd.asd',
            'firstname': 'zxc',
            'middlename': 'asd',
            'lastname': 'qwe',
            'comment': 'This is a test comment'
        }

        response = requests.post(self.reg_url)

        print(response.status_code)
        print(response.json())
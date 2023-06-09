from Pet_specification import PetSpecification
from selenium import webdriver

# values from sort fields in webpage
driver = webdriver.Firefox()
web_values = PetSpecification(driver)
web_values.values_from_page()
web_values.print_page_values()

# values from api for breeds
api_breeds = PetSpecification()
api_breeds.get_all_api_links()
api_breeds.get_api_values_to_list(n_link=1, n_page=4)

# values from api species
api_species = PetSpecification()
api_species.get_all_api_links()
api_species.get_api_values_to_list(n_link=3, n_page=6)

# values from api statuses
api_statuses = PetSpecification()
api_statuses.get_all_api_links()
api_statuses.get_api_values_to_list(n_link=2, n_page=2)

# values from api genders
api_genders = PetSpecification()
api_genders.get_all_api_links()
api_genders.get_api_values_to_list(n_link=4, n_page=3)

driver.quit()


def test_get_web_values():
    # test 5: get values from sorting fields.
    assert len(web_values.api_id_web_species) or len(web_values.api_name_web_breeds) or len(
        web_values.api_code_web_genders) != 0


def test_unique_web_species_values():
    # test 6: web species value should be unique - >
    # BUG_5: species values in webpage sort field are not unique
    un_len = web_values.get_unique_values(web_values.api_id_web_species)
    assert web_values.api_id_web_species == un_len


def test_unique_web_breeds_values():
    # test 7: web breeds value should be unique ->
    # BUG_6: breeds values in webpage sort field are not unique
    un_len = web_values.get_unique_values(web_values.api_name_web_breeds)
    assert web_values.api_name_web_breeds == un_len


def test_unique_web_genders_values():
    # test 8: web genders value should be unique
    # BUG_7: breeds values in webpage sort field are not unique
    un_len = web_values.get_unique_values(web_values.api_code_web_genders)
    assert web_values.api_code_web_genders == un_len
########################################################################
########################################################################
def test_get_api_breed_values():
    # test 9: get values from sorting fields.
    assert len(api_breeds.api_id_web_species) or len(api_breeds.api_name_web_breeds) or len(
        api_breeds.api_code_web_genders) != 0


def test_unique_api_breed_id():
    # test 10: api breed ID value should be unique
    un_len = api_breeds.get_unique_values(api_breeds.api_id_web_species)
    assert len(api_breeds.api_id_web_species) == len(un_len)


def test_unique_api_breed_name():
    # test 11: api breed NAME value should be unique ->
    # BUG_8: breed names values from API not unique
    un_len = api_breeds.get_unique_values(api_breeds.api_name_web_breeds)
    assert len(api_breeds.api_name_web_breeds) == len(un_len)


def test_unique_api_breed_code():
    # test 12: api breed CODE value should be unique ->
    # BUG_9: breed names values from API not unique
    un_len = api_breeds.get_unique_values(api_breeds.api_code_web_genders)
    assert len(api_breeds.api_code_web_genders) == len(un_len)
########################################################################
########################################################################
def test_get_api_species_values():
    # test 13: get api values from sorting fields.
    assert len(api_species.api_id_web_species) or len(api_species.api_name_web_breeds) or len(
        api_species.api_code_web_genders) != 0


def test_unique_api_species_id():
    # test 14: api species ID value should be unique
    un_len = api_species.get_unique_values(api_species.api_id_web_species)
    assert api_species.api_id_web_species == un_len


def test_unique_api_species_name():
    # test 15: api species NAME value should be unique ->
    # BUG_: species names values from API not unique
    un_len = api_species.get_unique_values(api_species.api_name_web_breeds)
    assert len(api_species.api_name_web_breeds) == len(un_len)


def test_unique_api_species_code():
    # test 16: api species CODE value should be unique ->
    # BUG_: species names values from API not unique
    un_len = api_species.get_unique_values(api_species.api_code_web_genders)
    assert len(api_species.api_code_web_genders) == len(un_len)
########################################################################
########################################################################
def test_get_api_statuses_values():
    # test 17: get api values for status.
    assert len(api_statuses.api_id_web_species) or len(api_statuses.api_name_web_breeds) or len(
        api_statuses.api_code_web_genders) != 0


def test_unique_api_statuses_id():
    # test 18: api statuses ID value should be unique
    un_len = api_statuses.get_unique_values(api_statuses.api_id_web_species)
    assert len(api_statuses.api_id_web_species) == len(un_len)


def test_unique_api_statuses_name():
    # test 19: api statuses NAME value should be unique ->
    # BUG_: statuses names values from API not unique
    un_len = api_statuses.get_unique_values(api_statuses.api_name_web_breeds)
    assert len(api_statuses.api_name_web_breeds) == len(un_len)


def test_unique_api_statuses_code():
    # test 20: api statuses CODE value should be unique ->
    # BUG_: statuses names values from API not unique
    un_len = api_statuses.get_unique_values(api_statuses.api_code_web_genders)
    assert len(api_statuses.api_code_web_genders) == len(un_len)
########################################################################
########################################################################
def test_get_api_genders_values():
    # test 21: get api values for genders.
    assert len(api_genders.api_id_web_species) or len(api_genders.api_name_web_breeds) or len(
        api_genders.api_code_web_genders) != 0


def test_unique_api_genders_id():
    # test 22: api genders ID value should be unique
    un_len = api_genders.get_unique_values(api_genders.api_id_web_species)
    assert len(api_genders.api_id_web_species) == len(un_len)


def test_unique_api_genders_name():
    # test 23: api genders NAME value should be unique ->
    # BUG_: genders names values from API not unique
    un_len = api_genders.get_unique_values(api_genders.api_name_web_breeds)
    assert len(api_genders.api_name_web_breeds) == len(un_len)


def test_unique_api_genders_code():
    # test 24: api genders CODE value should be unique ->
    # BUG_: genders names values from API not unique
    un_len = api_genders.get_unique_values(api_genders.api_code_web_genders)
    assert len(api_genders.api_code_web_genders) == len(un_len)
########################################################################
########################################################################


def test_breeds_compare_api_and_web():
    # test 25: BREED value from api should be the same as BREED in Page Sorting field
    # BUG_
    web_breeds = web_values.api_name_web_breeds
    assert web_breeds == api_breeds.api_name_web_breeds

def test_species_compare_api_web():
    # test 26: SPECIES value from api should be the same as SPECIES in Page Sorting field
    # BUG_
    web_species = web_values.api_id_web_species
    assert web_species == api_species.api_name_web_breeds

def test_gender_compare_api_web():
    # test 27 GENDER value from api should be the same as GENDER in Page Sorting field
    # BUG_ :
    web_genders = web_values.api_code_web_genders
    assert web_genders == api_genders.api_name_web_breeds
########################################################################
########################################################################

def test_post_new_breed_value(name="TEST_CORGI", code="TEST_BUM"):
    # test 28 post NEW breed value
    link = api_breeds.all_api_links[1]
    code = api_breeds.post_values_api(link, name, code)
    assert code == 200 or code == 201


def test_post_exist_breed_value():
    # test 29 post EXIST breed value should return code 400
    link = api_breeds.all_api_links[1]
    code = api_breeds.post_values_api(link)
    assert code == 400


def test_post_new_species_value(name="TEST_species", code="TTS"):
    # test 30 post NEW species value
    link = api_species.all_api_links[3]
    code = api_species.post_values_api(link, name, code)
    assert code == 200 or code == 201


def test_post_exist_species_value():
    # test 31 post EXIST species value should return code 400
    link = api_species.all_api_links[3]
    code = api_species.post_exist_value(link)
    assert code == 400


def test_post_new_status_value(name="TEST_status", code="TS"):
    # test 32 post NEW status value
    link = api_statuses.all_api_links[2]
    code = api_statuses.post_values_api(link, name, code)
    assert code == 200 or code == 201


def test_post_exist_status_value():
    # test 33 post EXIST status value should return code 400
    link = api_statuses.all_api_links[2]
    code = api_statuses.post_exist_value(link)
    assert code == 400


def test_post_new_gender_value(name="TEST_gender", code="TTGD"):
    # test 34 post NEW gender value
    link = api_genders.all_api_links[2]
    code = api_genders.post_values_api(link, name, code)
    assert code == 200 or code == 201


def test_post_exist_gender_value():
    # test 35 post EXIST gender value should return code 400
    link = api_genders.all_api_links[2]
    code = api_genders.post_exist_value(link)
    assert code == 400
########################################################################
########################################################################

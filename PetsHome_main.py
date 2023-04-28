from Header_links import Header
from Social_links import Social
from Pet_sorts import Sorting
from API_allvalues import APIValues


if __name__ == "__main__":
    p = Header()
    p.h_links()
    p.h_responses_titles()

    s = Social()
    s.s_links()

    so = Sorting()
    so.values_from_page()
    # numbers in params taken from POSTMAN
    pet_breeds = APIValues(num_link=1, num_page=4)
    pet_breeds.get_all_api_links()
    pet_breeds.get_api_values_to_list()
    pet_breeds.print_info()
    # ap.get_api_values_to_list(2, 2, ap.all_statuses)
    # ap.get_api_values_to_list(3, 6, ap.all_species)
    # ap.get_api_values_to_list(4, 3, ap.all_genders)



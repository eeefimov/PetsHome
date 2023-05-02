from Header_links import Header
from Social_links import Social
from Pet_sorts import Sorting
from Pet_specification import PetSpecification


if __name__ == "__main__":
    p = Header()
    p.h_links()
    p.h_responses_titles()

    s = Social()
    s.s_links()

    so = Sorting()
    so.values_from_page()

    # api_breeds = APIValues(num_link=1, num_page=4)
    # api_breeds.get_all_api_links()
    # # api_breeds.get_api_values_to_list()
    # # api_breeds.print_info()
    # ap.get_api_values_to_list(2, 2, ap.all_statuses)!
    # ap.get_api_values_to_list(3, 6, ap.all_species)!
    # ap.get_api_values_to_list(4, 3, ap.all_genders)



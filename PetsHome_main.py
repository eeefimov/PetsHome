from Header_links import Header
from Social_links import Social
from Pet_sorts import Sorting
from API_allvalues import APIValues


if __name__ == "__main__":
    p = Header()
    p.h_links()
    p.h_responses_titles()
    # p.links_print()

    s = Social()
    s.s_links()
    # s.slinks_print()

    so = Sorting()
    so.values_from_page()

    ap = APIValues()
    ap.get_all_api_links()
    # numbers in params taken from POSTMAN
    ap.get_api_values_to_list(1, 4, ap.all_breeds)
    ap.get_api_values_to_list(2, 2, ap.all_statuses)
    ap.get_api_values_to_list(3, 6, ap.all_species)
    ap.get_api_values_to_list(4, 3, ap.all_genders)



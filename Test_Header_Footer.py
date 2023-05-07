import pytest
from Header_links import Header
from Social_links import Social
# tests from 1 to 4 ( 2 BUGS)
HeaderPage = Header()
HeaderPage.h_links()
HeaderPage.h_responds_titles()

Footer = Social()
Footer.social_icon_links()


def test_represent_links():
    # test 1: get links from header of the page.
    assert len(HeaderPage.header_links) == 3


def test_header_links_code_200():
    # test 2 : checks status code 200 header links
    responds = HeaderPage.header_responds
    for i in range(0, len(responds)):
        code = str(responds.get(HeaderPage.header_links[i]))
        assert code == "<Response [200]>"


def test_tittles_of_header_links_():
    # test 3: check titles of header pages ->
    # BUG_1: all pages have the same title
    titles = HeaderPage.header_titles
    for i in range(0, len(titles)):
        unique_title = list(set(titles.get(HeaderPage.header_links[i])))
    assert len(unique_title) == 3


def test_social_icon_links():
    # test 4: check social links in footer icons ->
    # BUG_2: there are no links to social networks
    # set takes only one main links.
    links = Footer.social_links
    unique_social_links = set()
    unique_social_links.update(links)
    assert len(unique_social_links) == 4


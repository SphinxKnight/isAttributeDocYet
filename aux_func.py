#!/usr/bin/env python
'''Change functions here to adapt behavior of modules 
used within html_documented.'''

from bs4 import BeautifulSoup
import re

def filter_attributes(content_page):
    '''Input some html code from a page
    Output a list of documented attributes from this code
    According to some rules '''

    # The algorithm here is 
    # 1- find the Attributes H2 
    # 2- find the first definition list right after
    # 3- check for <a> element with attr-sthg as a name
    # 4- the text is the attribute we want
    my_soup = BeautifulSoup(content_page)
    my_soup.find(id = "Attributes")
    for sibling in my_soup.find(id = "Attributes").next_siblings:
        if(sibling.name == "dl"):
            dl_element = sibling
            break
    attributes_on_page = []
    all_a_with_attr = dl_element.find_all("a", attrs={"name": re.compile("attr")})
    for elem in all_a_with_attr:
        attributes_on_page.append(elem.get_text())
    return attributes_on_page

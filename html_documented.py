#!/usr/bin/env python
'''Script to see, from a json input file
if some attributes are documented in MDN
Return attributes that were *not* documented !'''

from sys import argv
from json import load, dumps
from urllib.request  import urlopen
from urllib import error
from aux_func import filter_attributes

#Fixed variables 
# 1- the base URL where we fetch the page 
BASE_URL = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/"

def main():
    '''Main and simple algorithm depending 
    heavily on aux_func.filter_attributes
    for hard work'''

    # Argument 1 : input file json 
    input_file = open(argv[1])
    list_error_pages = []
    final_dict = dict()

    html_elements = load(input_file)
    for tuple_el in html_elements:
        (html_el, list_att) = (tuple_el["element"], tuple_el["attributes"])
        
        try:
            # For each HTML element we fetch the page 
            url_request = urlopen(BASE_URL+html_el)
            content_page = url_request.read().decode('utf-8')
            # We get the attributes documented on this page
            attributes_on_page = filter_attributes(content_page)
            #Compare the list with the json input
            delta_input_doc = list(set(list_att)-set(attributes_on_page))
            final_dict.setdefault(html_el, delta_input_doc)

        except (error.HTTPError, error.URLError):
            # print("Urllib error (?Connection?):"+html_el)
            list_error_pages.append(html_el)

    print(dumps(final_dict))
    return final_dict


if __name__ == "__main__":
    main()


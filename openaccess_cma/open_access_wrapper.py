import inspect
import requests
import openaccess_cma.constants as c
from openaccess_cma.error_checking import validate_arguments
import unittest


#This is a simple wrapper function for making requests
#to Cleveland Museum of Art's open-access API. Documentation
#for the API can be found here http://openaccess-api.clevelandart.org/
def openaccess_cma_search(**kwargs):
    #validating provided keyword arguments
    for k in kwargs.keys():
      if k not in c.VALID_PARAMETERS:
        raise TypeError("openaccess_cma_search got an unexpected keyword argument : '%s'"%(k))
    API_BASE_URL = "https://openaccess-api.clevelandart.org/api/artworks/?"
    API_REQUEST = API_BASE_URL
    #error checking for arugments
    validate_arguments(kwargs)
    #local function for adding parameters to query string
    def add_query(query_type, argument):
        if argument is not None:
            nonlocal API_REQUEST
            str_argument = str(argument)
            q = ""
            if query_type in c.NO_ARGUMENT:
                if bool(argument):
                    q = query_type+'&'
            else:
                q = query_type+'='+str_argument+'&'
            API_REQUEST += q
    #looping through arguments and generating query
    for k, v in kwargs.items():
        add_query(k, v)
    #remove trailing '&' if one exists
    if API_REQUEST[-1] == '&':
        API_REQUEST = API_REQUEST[:-1]
    #making the requests
    r = requests.get(API_REQUEST)
    if r.status_code != requests.codes.ok:
        raise requests.HTTPError(c.BAD_REQUEST(r.status_code))
    return r.json(), API_REQUEST

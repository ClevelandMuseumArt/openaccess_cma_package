import inspect
import requests
import openaccess_cma.constants as c
from openaccess_cma.error_checking import validate_arguments
import unittest


#This is a simple wrapper function for making requests
#to Cleveland Museum of Art's open-access API. Documentation
#for the API can be found here http://openaccess-api.clevelandart.org/
def openaccess_cma_search(q=None,
                          cc0=None,
                          department=None,
                          type=None,
                          has_image=None,
                          indent=None,
                          skip=None,
                          limit=None,
                          artists=None,
                          title = None,
                          medium = None,
                          credit = None,
                          catalogue_raisonne = None,
                          provenance = None,
                          citations = None,
                          exhibition_history = None,
                          created_before = None,
                          created_after = None,
                          currently_on_loan = None,
                          currently_on_view = None,
                          african_american_artists = None,
                          cia_alumni_artists = None,
                          may_show_artists = None,
                          female_artists = None,
                          recently_acquired = None,
                          nazi_era_provenance = None,
                          created_after_age = None,
                          created_before_age = None,
                          ):
    #generates a dictionary of argument value pairs
    _, _, _, values = inspect.getargvalues(inspect.currentframe())
    API_BASE_URL = "https://openaccess-api.clevelandart.org/api/artworks/?"
    API_REQUEST = API_BASE_URL
    #error checking for arugments
    validate_arguments(values)
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
    for k, v in values.items():
        add_query(k, v)
    if API_REQUEST[-1] == '&':
        API_REQUEST = API_REQUEST[:-1]
    #making the requests
    r = requests.get(API_REQUEST)
    if r.status_code != requests.codes.ok:
        raise requests.HTTPError(c.BAD_REQUEST(r.status_code))
    return r.json(), API_REQUEST

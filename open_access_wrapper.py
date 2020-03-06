import inspect
import requests
import constants as c
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
                          limit=None):
    #generates a dictionary of argument value pairs
    _, _, _, values = inspect.getargvalues(inspect.currentframe())
    API_BASE_URL = "https://openaccess-api.clevelandart.org/api/artworks/?"
    API_REQUEST = API_BASE_URL

    #Error Checking
    if limit is not None:
        try:
            if int(limit) < 0:
                raise ValueError("Limit cannot be less than zero")
        except ValueError:
            raise ValueError("Limit must be able to be cast to an integer")

    if cc0 is not None:
        if str(cc0) not in c.VALID_CC0_TYPES:
            raise ValueError(c.CC0_ERROR_MESSAGE)

    if department is not None:
        if str(department) not in c.VALID_DEPARTMENTS:
            raise ValueError(c.DEPARTMENT_ERROR_MESSAGE)

    if type is not None:
        if str(type) not in c.VALID_TYPES:
            raise ValueError(c.TYPE_ERROR_MESSAGE)

    #local function for adding parameters to query string
    def add_query(query_type, argument):
        if argument is not None:
            nonlocal API_REQUEST
            argument = str(argument)
            q = query_type+'='+argument+'&'
            API_REQUEST += q

    for k, v in values.items():
        add_query(k, v)
    r = requests.get(API_REQUEST)
    if r.status_code != requests.codes.ok:
        raise requests.HTTPError(c.ERROR_MESSAGE)
    return r.json(), API_REQUEST


if __name__ == "__main__":
    import tests
    unittest.main()

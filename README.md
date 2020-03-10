# Cleveland Museum of Art's Open Access API Python ModuleThis python module provides a wrapper function with error checking for the CMA open access API, [API documentation can be found here](http://openaccess-api.clevelandart.org/). The function returns a tuple containing in the first entry a python dictionary representing the Open Access API's JSON response to the query, and in the second value the URL used to make the query. The wrapper function is 	openaccess_cma_search() An example usage of the function is,	d, q = openaccess_cma_search(q="monet", limit="10") Please see [CMA's open-access API documentation](http://openaccess-api.clevelandart.org/) for a full list of arguments to the wrapper function. The function implements all parameters specified in the API documentation.For API parameters that take no argument such as "female_artists", the function will include the parameter if given any argument that when cast as a Boolean returns true. For example, 	d, q = openaccess_cma_search(female_artists="True",limit=1)	print(q)will output ...	https://openaccess-api.clevelandart.org/api/artworks/?cia_alumni_artists&limit=1And	d, q = openaccess_cma_search(female_artists=0,limit=1)	print(q)will output...	https://openaccess-api.clevelandart.org/api/artworks/?limit=1## ExamplesReturns three artworks acquired by CMA produced by African American Cleveland Institute of Art alumni.	d,q = openaccess_cma_search(african_american_artists=True, cia_alumni_artists="1", limit=3)Returns all CMA artworks produced by Picasso that are connected with Nazi art looting.	d,q = openaccess_cma_search(artists="Picasso", nazi_era_provenance = 1)Returns the maximum number of CMA artworks obtainable in one query (1000) produced by African American artists. 	d,q = openaccess_cma_search(female_artists="A string that is true")
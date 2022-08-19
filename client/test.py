import mano_api
from mano_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mano_api.Configuration(host="http://127.0.0.1:8000")


# Enter a context with an instance of the API client
with mano_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Admins
        api_response = api_instance.get_admins_v1_admins_admins_get()
        pprint(api_response)
    except mano_api.ApiException as e:
        print("Exception when calling DefaultApi->get_admins_v1_admins_admins_get: %s\n" % e)
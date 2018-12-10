# Third-party imports...
from nose.tools import assert_equals

# Local imports...
from services import get_dogs


def test_request_response():
    # Call the service, which will send a request to the server.
    response = get_dogs()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_equals(200, response.status_code)


""" Todo: Inspect Json Result for Retriever"""

""" Todo: Get all sub-breeds for Retriever"""

""" Get random link for golden in retriever sub-breed """

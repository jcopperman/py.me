# Third party libraries...
from behave import given, then
from nose.tools import assert_equals, assert_true

# Local imports...
from tests.api import get_dogs, get_sub_breed, get_random_image_in_sub_breed
from data.constants import BREED_QUERY


# Variables...
response = get_dogs()
query_breed = get_sub_breed()
breed_random_image = get_random_image_in_sub_breed()
breed = BREED_QUERY
regex_pattern = response.text;


# Tests...
@given(u'Perform an API request to produce a list of all dog breeds.')
def test_request_list_all_breeds():
    assert_equals(200, response.status_code)


@given(u'Using code, verify “retriever” breed is within the list.')
def test_request_query_sub_breed_in_breeds():
    assert_true(breed in response.text)


@given(u'Perform an API request to produce a list of sub-breeds for “retriever”.')
def test_request_list_sub_breeds():
    assert_equals(200, query_breed.status_code)


@then(u'Perform an API request to produce a random image / link for the sub-breed “golden”')
def test_request_random_image():
    assert_equals(200, breed_random_image.status_code)

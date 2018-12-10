# Third-party imports...
from nose.tools import assert_equals, assert_true

# Local imports...
from services import get_dogs, get_sub_breed, get_random_image_in_sub_breed
from constants import BREED_QUERY


response = get_dogs()
query_breed = get_sub_breed()
breed_random_image = get_random_image_in_sub_breed()
breed = BREED_QUERY


def test_request_list_all_breeds():
    assert_equals(200, response.status_code)


def test_request_query_sub_breed_in_breeds():
    assert_true(breed in response.text)


def test_request_list_sub_breeds():
    assert_equals(200, query_breed.status_code)


def test_request_random_image():
    assert_equals(200, breed_random_image.status_code)





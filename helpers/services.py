# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests
import json

# Local imports...
from data.constants import BASE_URL, BREED_QUERY

BREED_TEST_URL = urljoin(BASE_URL, 'api/breeds/list/all')
SUB_BREED_TEST_URL = urljoin(BASE_URL, '/api/breed/' + BREED_QUERY + '/list')
RANDOM_IMAGE_URL = urljoin(BASE_URL, 'api/breed/' + BREED_QUERY + '/images/random')
BREED = BREED_QUERY


def get_dogs():
    response = requests.get(BREED_TEST_URL)
    if response.ok:
        return response
    else:
        return None


def get_sub_breed():
    response = requests.get(SUB_BREED_TEST_URL)
    if response.ok:
        return response
    else:
        return None


def get_random_image_in_sub_breed():
    response = requests.get(RANDOM_IMAGE_URL)
    if response.ok:
        print(response.text)
        return response
    else:
        return None


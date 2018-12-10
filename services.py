# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
from constants import BASE_URL

TEST_URL = urljoin(BASE_URL, 'api/breeds/list/all')


def get_dogs():
    response = requests.get(TEST_URL)
    if response.ok:
        return response
    else:
        return None

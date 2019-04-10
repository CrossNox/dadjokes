import requests
from dadjokes import USER_AGENT
from abc import ABCMeta as ABC, abstractmethod

HEADERS = {'User-Agent': USER_AGENT}
BASE_URL = "https://icanhazdadjoke.com/"

TEXT = 'text/plain'
JSON = 'application/json'


def get_headers(accept):
    h = dict(HEADERS)
    h['Accept'] = accept
    return h


class AbstractDadJoke:
    @property
    @abstractmethod
    def id(self):
        pass

    @property
    @abstractmethod
    def joke(self):
        pass


class Dadjoke(AbstractDadJoke):
    def __init__(self):
        self._jokeid = None
        self._joke = None

    def _get_joke(self):
        url = BASE_URL
        response = requests.get(url, headers=get_headers(JSON))
        response = response.json()
        self._jokeid = response['id']
        self._joke = response['joke']

    @property
    def id(self):
        if self._jokeid is None:
            raise AttributeError("I haz no id yet! I can't AID you")
        return self._jokeid

    @property
    def joke(self):
        if not self._joke:
            self._get_joke()
        return self._joke

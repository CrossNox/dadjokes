import requests
from dadjokes import USER_AGENT, BASE_URL, HEADERS
import urllib
from functools import lru_cache


@lru_cache(maxsize=128)
def cached_request(url):
    return requests.get(url, headers=HEADERS)


class DadjokeSearch:
    def __init__(self, term=None, limit=None):
        url = BASE_URL + 'search'
        if term:
            url += '?'
            url += urllib.parse.urlencode({'term': term})
        self.url = url
        self.limit = limit

    def __next__(self):
        return self

    def __iter__(self):
        r = cached_request(self.url).json()
        joked = 0
        while r:
            for result in r['results']:
                if joked == self.limit:
                    break
                dj = Dadjoke()
                dj._joke = result['joke']
                dj._jokeid = result['id']
                joked += 1
                yield dj
            if r['current_page'] == r['total_pages']:
                r = None
            elif joked != self.limit:
                r = None
            else:
                r = cached_request(self.url).json()


class Dadjoke:
    def __init__(self, jokeid=None):
        self._jokeid = jokeid
        self._joke = None

    @classmethod
    def _req(cls, url, cached=True):
        if not cached:
            return requests.get(url, headers=HEADERS)
        return cached_request(url)

    def _get_joke(self):
        url = BASE_URL
        response = Dadjoke._req(url, cached=False)
        response = response.json()
        self._jokeid = response['id']
        self._joke = response['joke']

    def _fetch_joke(self):
        url = BASE_URL + 'j/' + self._jokeid
        response = Dadjoke._req(url)
        response = response.json()
        self._joke = response['joke']

    # hey, at least i don't need to call the api
    @property
    def as_slack(self):
        joke = self.joke
        reponse = {'attachments': [
            {
                'fallback': joke,
                'footer': ' - ',
                'text': joke
            }
        ],
            'response_type': 'in_channel',
            'username': 'dadjokes'}
        return reponse

    @property
    def id(self):
        if self._jokeid is None:
            raise AttributeError("I haz no id yet! I can't AID you")
        return self._jokeid

    @property
    def joke(self):
        if not self._joke:
            if self._jokeid:
                self._fetch_joke()
            else:
                self._get_joke()
        return self._joke

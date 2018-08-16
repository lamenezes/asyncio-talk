import sys

import requests

from utils import timeit


@timeit()
def get(url, session):
    # requests cria uma nova sessão para cada request
    response = session.get(url)
    print(response.status_code, end='\t')


@timeit(prefix='total getn\t')
def getn(url, n):
    session = requests.Session()
    for i in range(1, n + 1):
        print(i, end='\t')
        get(url, session)


if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except (ValueError, IndexError):
        n = 10

    url = 'https://httpbin.org/get'

    print('sync fetch {}x {!r}'.format(n, url))
    getn(url, n)

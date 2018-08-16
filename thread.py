from threading import Thread

import sync


if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    print('thread fetch 10x {!r}'.format(url))

    threads = (
        Thread(target=sync.getn, kwargs={'url': url, 'n': 4}),
        Thread(target=sync.getn, kwargs={'url': url, 'n': 3}),
        Thread(target=sync.getn, kwargs={'url': url, 'n': 3}),
    )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

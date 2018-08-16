import time
from contextlib import contextmanager


@contextmanager
def timeit(prefix=None):
    t0 = time.time()
    yield
    ellapsed = time.time() - t0

    if prefix:
        print(prefix, end='')
    print('ellapsed={:.2f}s'.format(ellapsed))

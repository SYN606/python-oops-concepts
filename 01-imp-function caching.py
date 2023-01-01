# function caching 

"""
    for futhur details please checkout : https://medium.com/fintechexplained/advanced-python-how-to-implement-caching-in-python-application-9d0a4136b845
"""

import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    # some task taking n second 
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("done.... Calling again")
    some_work(3)
    print("Called again")

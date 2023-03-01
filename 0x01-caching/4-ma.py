#!/usr/bin/python3
"""
Test
"""
import sys

try:
    MRUCache = __import__('4-mru_cache').MRUCache
    from base_caching import BaseCaching

    BaseCaching.MAX_ITEMS = 1
    MRUCache.MAX_ITEMS = 1
    my_cache = MRUCache()
    my_cache.MAX_ITEMS = 1
    prev_key = None
    
    for i in range(2):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        if prev_key is not None:
            my_cache.get(key)
        prev_key = key
        my_cache.put(key, value)
        my_cache.print_cache()

except:
    print(sys.exc_info()[1])
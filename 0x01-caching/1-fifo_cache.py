#!/usr/bin/env python3
"""FIFOCache algorithm
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using FIFOCache Algorithm
    """

    def __init__(self):
        """calling the parent class
        """
        super().__init__()

    def put(self, key, item):
        """ It will assign to self.cache_data
        form the parent class"""
        if (key is not None and item is not None):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                item_to_del = list(self.cache_data.items())[0][0]
                del self.cache_data[item_to_del]
                print("DISCARD: {}".format(item_to_del))

    def get(self, key):
        """ Return the value in self.cach_data
        linked to key"""
        if (self.cache_data.get(key, None)):
            return (self.cache_data.get(key))
        return (None)

#!/usr/bin/env python3
"""LIFOCache Algorithm
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using LIFOCache Algorithm
    """
    item_to_del = ""

    def __init__(self):
        """calling the parent class
        """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data
        the item value for the key"""
        if (key is not None and item is not None):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                del self.cache_data[LIFOCache.item_to_del]
                print("DISCARD: {}".format(LIFOCache.item_to_del))
            LIFOCache.item_to_del = key

    def get(self, key):
        """ Must return the value in self.cache_data linked to key
        """
        if (self.cache_data.get(key, None)):
            return (self.cache_data.get(key))
        return (None)

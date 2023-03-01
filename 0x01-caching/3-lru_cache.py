#!/usr/bin/env python3
"""LRUCache Algorithm
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using LIFOCache Algorithm
    """
    item_used = []

    def __init__(self):
        """calling the parent class
        """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data
        the item value for the key"""
        if (key is not None and item is not None):
            self.cache_data[key] = item

            if (key in LRUCache.item_used):
                LRUCache.item_used.remove(key)
                LRUCache.item_used.append(key)
            else:
                LRUCache.item_used.append(key)

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):

                del self.cache_data[LRUCache.item_used[0]]
                print("DISCARD: {}".format(LRUCache.item_used[0]))
                LRUCache.item_used.pop(0)

    def get(self, key):
        """ Must return the value in self.cache_data linked to key
        """
        if (self.cache_data.get(key, None)):
            LRUCache.item_used.remove(key)
            LRUCache.item_used.append(key)
            return (self.cache_data.get(key))
        return (None)

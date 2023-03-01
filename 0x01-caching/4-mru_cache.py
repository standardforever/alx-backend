#!/usr/bin/env pythondet
"""MRUCache Algorithm
"""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using MRUCache Algorithm
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

            if (key in MRUCache.item_used):
                MRUCache.item_used.remove(key)
                MRUCache.item_used.append(key)
            else:
                MRUCache.item_used.append(key)

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                det = BaseCaching.MAX_ITEMS - 1
                del self.cache_data[MRUCache.item_used[det]]
                print("DISCARD: {}".format(MRUCache.item_used[det]))
                MRUCache.item_used.pop(det)

    def get(self, key):
        """ Must return the value in self.cache_data linked to key
        """
        if (self.cache_data.get(key, None)):
            MRUCache.item_used.remove(key)
            MRUCache.item_used.append(key)
            return (self.cache_data.get(key))
        return (None)

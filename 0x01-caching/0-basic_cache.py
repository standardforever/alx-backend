#!/usr/bin/env python3
""" Basic caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - BasicCache Algorithm
    """

    def __init__(self):
        """ Initalization
        """
        super().__init__()

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data the item value
        for the key key.
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key
        """
        if (self.cache_data.get(key, None)):
            return (self.cache_data.get(key))
        return (None)

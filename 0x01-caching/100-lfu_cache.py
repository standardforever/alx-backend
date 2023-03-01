#!/usr/bin/env python3
"""LFUCache Algorithm
"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using LIFOCache Algorithm
    """
    item_count = {}
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

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                value = sorted(LFUCache.item_count.values())
                if (len(value) > 1 and value[0] == value[1]):
                    to_delete = ''
                    items = LFUCache.item_used
                    index = 0
                    for i in range(BaseCaching.MAX_ITEMS):
                        if (LFUCache.item_count[items[i]] == value[0]):
                            to_delete = items[i]
                            index = i
                            break

                    del self.cache_data[to_delete]
                    del LFUCache.item_count[to_delete]
                    print("DISCARD: {}".format(to_delete))
                    LFUCache.item_used.pop(index)

                else:
                    sm = min(LFUCache.item_count, key=LFUCache.item_count.get)
                    del self.cache_data[sm]
                    del LFUCache.item_count[sm]
                    LFUCache.item_used.remove(sm)
                    print("DISCARD: {}".format(sm))

            if (key in LFUCache.item_count):
                count = LFUCache.item_count.get(key)
                LFUCache.item_count[key] = count + 1

                LFUCache.item_used.remove(key)
                LFUCache.item_used.append(key)

            else:
                LFUCache.item_count[key] = 0
                LFUCache.item_used.append(key)

    def get(self, key):
        """ Must return the value in self.cache_data linked to key
        """
        if (self.cache_data.get(key, None)):
            count = LFUCache.item_count.get(key)
            LFUCache.item_count[key] = count + 1

            LFUCache.item_used.remove(key)
            LFUCache.item_used.append(key)
            return (self.cache_data.get(key))
        return (None)

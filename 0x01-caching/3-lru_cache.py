#!/usr/bin/env python3
''' implements LRU caching'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system'''

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        ''' Assign the item to key of a dictionary '''
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.order.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Return the value linked to a key '''
        if key and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

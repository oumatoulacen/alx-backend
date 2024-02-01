#!/usr/bin/env python3
''' implements LIFO caching'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system'''
    def __init__(self):
        ''' initializes the cache'''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        ''' puts item in cache'''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.stack.pop()
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))
            if key in self.cache_data:
                self.stack.remove(key)
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' gets item from cache'''
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

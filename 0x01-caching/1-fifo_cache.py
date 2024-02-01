#!/usr/bin/env python3
''' implements FIFO caching'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system'''
    def __init__(self):
        ''' initializes the cache'''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        ''' puts item in cache'''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))
            if key in self.cache_data:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' gets item from cache'''
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

#!/usr/bin/env python3
''' implements LFU caching'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system'''

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.order = []
        self.times = {}

    def put(self, key, item):
        ''' Assign the item to key of a dictionary '''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.order.pop(0)
                self.order.sort(key=lambda k: self.times.get(
                    k) if self.times.get(k) is not None else 1)
                check = self.times.get(discard)
                if check is not None and check > 1:
                    discard = self.order.pop(0)
                if discard in self.times:
                    del self.times[discard]
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))
            if key in self.cache_data:
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Return the value linked to a key '''
        if key and key in self.cache_data:
            self.times[key] = self.times[key] + 1 if key in self.times else 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

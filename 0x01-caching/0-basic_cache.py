#!/usr/bin/env python3
''' implements basic caching'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system'''
    def put(self, key, item):
        ''' puts item in cache'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' gets item from cache'''
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

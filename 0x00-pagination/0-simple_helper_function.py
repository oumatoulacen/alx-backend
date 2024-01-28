#!/usr/bin/env python3
'''helper function file'''


def index_range(page, page_size):
    '''takes two integer arguments page and page_size'''
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return (first_index, last_index)

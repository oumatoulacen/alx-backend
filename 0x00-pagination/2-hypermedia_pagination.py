#!/usr/bin/env python3
'''module for task 2'''
import csv
import math
from typing import List


def index_range(page, page_size):
    '''takes two integer arguments page and page_size'''
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return (first_index, last_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Get a list of the correct page'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        first_idx, last_idx = index_range(page, page_size)
        return self.dataset()[first_idx:min(last_idx, len(self.dataset()))]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''Get a dictionary of the correct page'''
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

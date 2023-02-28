#!/usr/bin/env python3
"""
hypermedia pagination
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Return tuple of index of pagination parameter"""
        new_tuple = ((page - 1) * page_size, page_size * page)

        return (tuple(new_tuple))

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
        """it returns a list of page requested
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        page_size > 0
        rang = Server.index_range(page, page_size)
        data = self.dataset()
        try:
            return (data[rang[0]:rang[1]])
        except IndexError:
            return ([])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """it returns details about the page
        """
        pages = self.get_page(page, page_size)
        new_dict = {"page": page, "page_size": len(pages), "data": pages, }
        if (page > 1):
            new_dict["prev_page"] = page - 1
        else:
            new_dict["prev_page"] = None
        if (len(self.get_page(page + 1, page_size))) == 0:
            new_dict["next_page"] = None
        else:
            new_dict["next_page"] = page + 1

        i = 1
        while (len(self.get_page(i, page_size)) != 0):
            i += 1
        new_dict["total_pages"] = i - 1
        return (new_dict)

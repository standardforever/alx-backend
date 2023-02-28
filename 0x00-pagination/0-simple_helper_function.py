#!/usr/bin/env python3
"""Pagination in python"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return tuple of index of pagination parameter"""
    new_tuple = ((page - 1) * page_size, page_size * page)
    return (tuple(new_tuple))

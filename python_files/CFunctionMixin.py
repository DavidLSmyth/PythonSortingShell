#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:32:11 2017

@author: david
"""

import collections
import ctypes

class CFunctionMixin():
    def load_c_function(self, function_name: str):
        try:
            sorting_lib = ctypes.CDLL("./c_code/libsorting_functions.so")
            sorting_algo = eval('sorting_lib.{}'.format(function_name))      
            sorting_algo.restype = None
            sorting_algo.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
        except FileNotFoundError as e:
            print(f'could not load {function_name}')
            raise e
        return sorting_algo
    
    def prepare_c_int_array(self, iterable: collections.Iterable)->collections.Iterable:
        my_array_type = ctypes.c_int * len(iterable)
        new_iterable = my_array_type()
        new_iterable[0:] = iterable
        return new_iterable
    
    def sort(self, iterable):
        '''An abstration of the base class sort method. Given a __repr__ that is a valid
        c sorting function, will return the sorted iterable according to the method'''
        sorting_method = self.load_c_function(self.__repr__())
        c_iterable = self.prepare_c_int_array(iterable)
        sorting_method(c_iterable, len(c_iterable))
        return list(c_iterable)
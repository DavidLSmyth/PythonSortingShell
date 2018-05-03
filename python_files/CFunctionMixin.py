#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:32:11 2017

@author: david
"""

import collections
import ctypes
import os
import subprocess
import platform
import sys

class CFunctionMixin():
    #pre-initialisation loads in c sorting library pre-emptively
    c_modules_compiled = False
    plat = platform.platform().lower()
    print('Platform: ', plat)
    #def __setup(self):
    print(os.path.abspath(os.curdir + '/..'))
    if 'windows' in plat:
        if not c_modules_compiled:
            print('Rebuilding windows sorting dll')
            os.chdir('..\\c_code')
            subprocess.call(["make", "-f", "MakeFileWin", "clean"])
            subprocess.call(["make", "-f", "MakeFileWin"])
            os.chdir('..\\python_files')
            c_modules_compiled = True
        else:
            print("C functions have already been loaded")
            #c modules have already been compiled

        try:
            print('printing sortinglib')
            print(open(os.path.abspath(os.curdir + '/..') + "/c_code/sorting_functions.c").read())
            sorting_lib = ctypes.cdll.LoadLibrary('../c_code/libsorting_functions.dll')
            print(dir(sorting_lib))
        except OSError as e:
            print('Could not load libsorting_functions.dll')
            raise e

    elif 'linux' in plat:
        if not c_modules_compiled:
            print('Rebuilding linux sorting dll')
            os.chdir('../c_code')
            subprocess.call(["make", "-f", "MakeFileLinux", "clean"])
            subprocess.call(["make", "-f", "MakeFileLinux"])
            os.chdir('../python_files')
            c_modules_compiled = True
        else:
            print("C functions have already been loaded")
            #c modules have already been compiled

        try:
            print('printing sortinglib')
            print(open(os.path.abspath(os.curdir + '/..') + "/c_code/sorting_functions.c").read())
            sorting_lib = ctypes.CDLL(os.path.abspath(os.curdir + '/..') + "/c_code/libsorting_functions.so")
            print(dir(sorting_lib))
        except OSError as e:
            print('Could not load libsorting_functions.so')
            raise e

    else:
        raise Exception('Could not detect OS to load sorting library')


    def load_c_function(self, function_name: str) -> 'function':
        '''Loads a c function - this is system dependent'''
        #self.__setup()
        return self._load_c_sorting_function(function_name)

    def _load_c_sorting_function(self, function_name):
        try:
            sorting_algo = eval('CFunctionMixin.sorting_lib.{}'.format(function_name))
            sorting_algo.restype = None
            sorting_algo.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
            return sorting_algo
        except Exception as e:
            print('Could not load {}'.format(function_name))
            raise e

    # def _load_c_sorting_function_windows(self, function_name: str):
    #     print('rebuilding code')
    #     os.chdir('..\\c_code')
    #     subprocess.call(["make", "-f", "MakeFileWin", "clean"])
    #     subprocess.call(["make", "-f", "MakeFileWin"])
    #     os.chdir('..\\python_files')
    #     try:
    #         sorting_lib = ctypes.cdll.LoadLibrary('../c_code/libsorting_functions.dll')
    #         return self._load_c_function(function_name, sorting_lib)
    #     except OSError as e:
    #         print('could not load {} from file c_code/libsorting_functions.so'.format(function_name))
    #         raise e
    #
    # def _load_c_sorting_function_linux(self, function_name: str):
    #     print('rebuilding code')
    #     os.chdir('..\\c_code')
    #     subprocess.call(["make", "-f", "MakeFileLinux", "clean"])
    #     subprocess.call(["make", "-f", "MakeFileLinux"])
    #     os.chdir('..\\python_files')
    #     try:
    #         #os.chdir(os.curdir)
    #         sorting_lib = ctypes.CDLL("../c_code/libsorting_functions.so")
    #         return self._load_c_function(function_name, sorting_lib)
    #     except OSError as e:
    #         print('could not load {} from file c_code/libsorting_functions.so'.format(function_name))
    #         raise e


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
    
    #ToDo
    def get_source(self):
        raise NotImplementedError('Havent found a way to retrieve c code yet')
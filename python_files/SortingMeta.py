# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:55:04 2017

@author: 13383861
"""

class SortingMeta(type):
    #extend functionality of new
    def __new__(cls, name, bases, body):
        #Force subclasses to have sort method
        #kind of like java interface
        if name != 'SortingBase' and not 'sort' in body:
            raise TypeError('{} is not a valid derived sorting class'.format(name))
        return super().__new__(cls,name,bases,body)
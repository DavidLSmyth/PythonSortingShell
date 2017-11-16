#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:42:29 2017

@author: david
"""
from Sorter import Sorter

def main():
    test_sorter = Sorter()
    test_sorter.load_sorting_method('QuickSort')
#    test_sorter.load_all_methods()
#    test_sorter.unload_sorting_method('MergeSortRecursive')
#    test_sorter.unload_sorting_method('BubbleSortRecursive')
#    test_sorter.plot_timings(False,'demo')
#    test_sorter.unload_sorting_method('BubbleSort')
#    test_sorter.plot_timings(False, 'demo1')
    test_sorter.unload_all_loaded_methods()
    test_sorter.load_c_methods()
    test_sorter.plot_timings(False, 'c_only', True)

if __name__ == '__main__':
    main()
    
#with open('/home/david/Dropbox/SoftwareDevelopment/PythonSortingShell/PythonSortingShell/requirements.txt') as f1, open('/home/david/Dropbox/SoftwareDevelopment/PythonSortingShell/PythonSortingShell/README.md') as f2:
#    for line1, line2 in zip(f1.readlines(), f2.readlines()):
#        print(line1, line2)
#        
#import pandas as pd
#import numpy as np
#df = pd.DataFrame({'A':[i for i in range(100)]+[np.NaN]})
#True in df.isnull()
#df.isnull().any()
#
#
#import math
#
#def binom(a,b):
#    return(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))
#
#
#print(sum([binom(400,i)*(0.1**(i))*(0.9**(400-i)) for i in range(50,400)]))

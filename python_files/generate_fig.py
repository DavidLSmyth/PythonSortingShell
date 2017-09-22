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
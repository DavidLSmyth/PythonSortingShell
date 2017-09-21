#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:42:29 2017

@author: david
"""
from Sorter import Sorter

test_sorter = Sorter()
test_sorter.load_sorting_method('QuickSort')
test_sorter.load_all_methods()
#test_sorter._loaded_sorting_methods
#test_sorter._get_available_sorting_methods()
test_sorter.unload_sorting_method('MergeSortRecursive')
test_sorter.unload_sorting_method('BubbleSortRecursive')
test_sorter.plot_timings(False,True)

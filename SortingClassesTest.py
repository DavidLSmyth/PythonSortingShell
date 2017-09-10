# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:02:05 2017

@author: 13383861
"""

import unittest
import random

from SortingBase import SortingBase
from SortingClasses import *

class SortingTest(unittest.TestCase):
    
    def test_sorting_method(self, sorting_method):
        print('testing',sorting_method.__repr__())
        l = [random.randint(-1000,1000) for i in range(50)]
        self.assertEqual(sorted(l), sorting_method.sort(l))
    
    def test_mergesort(self):
        x = MergeSort(False)
        self.test_sorting_method(x)
        
      
    def test_bubblesort(self):
        x = BubbleSort(False)
        self.test_sorting_method(x)
#        x = BubbleSort(False)
#        l = [random.randint(-1000,1000) for i in range(50)]
#        self.assertEqual(sorted(l), x.sort(l))
        
    def test_bubblesort_recursive(self):
        x = BubbleSortRecursive(False)
        l = [random.randint(-1000,1000) for i in range(50)]
        self.assertEqual(sorted(l), x.sort(l))
        
    def test_mergesort_recursive(self):
        x = MergeSortRecursive(False)
        l = [random.randint(-1000,1000) for i in range(50)]
        self.assertEqual(sorted(l), x.sort(l))
        
    def test_insertionsort(self):
        x = InsertionSort(False)
        l = [random.randint(-1000,1000) for i in range(33)]
        self.assertEqual(sorted(l), x.sort(l))
        
    def test_merge(self):
        ll = sorted([random.randint(-1000,1000) for i in range(50)])
        rl = sorted([random.randint(-1000,1000) for i in range(50)])
        self.assertEqual(sorted(ll+rl), SortingBase.merge(ll,rl))
        

        
    def test_binary_search(self):
        l = [1,2,3,5,6]
        element = 4
        self.assertEqual(-4, SortingBase.binary_search(l, element))
        l=[4,6,8,9,12,14,15]
        element = 15
        self.assertEqual(6, SortingBase.binary_search(l, element))

        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:02:05 2017

@author: 13383861
"""

import unittest
import random

from SortingBase import * 
from SortingClasses import *

class SortingTest(unittest.TestCase):
    
    def test_mergesort(self):
        x = MergeSort(False)
        l = [random.randint(-1000,1000) for i in range(50)]
        self.assertEqual(sorted(l), x.sort(l))
      
    def test_bubblesort(self):
        x = BubbleSort(False)
        l = [random.randint(-1000,1000) for i in range(50)]
        self.assertEqual(sorted(l), x.sort(l))
        
    def test_bubblesort_recursive(self):
        x = BubbleSortRecursive(False)
        l = [random.randint(-1000,1000) for i in range(50)]
        self.assertEqual(sorted(l), x.sort(l))
        
    def test_mergesort_recursive(self):
        x = MergeSortRecursive(False)
        l = [random.randint(-1000,1000) for i in range(50)]
        self.assertEqual(sorted(l), x.sort(l))
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
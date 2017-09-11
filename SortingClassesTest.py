# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:02:05 2017

@author: 13383861
"""

import unittest
import random
import math

from SortingBase import SortingBase
from SortingClasses import MergeSort, MergeSortRecursive, BubbleSort, BubbleSortRecursive, InsertionSort, QuickSort

class SortingTest(unittest.TestCase):
    
    def helper_sorting_method(self, sorting_class):
        '''Each sorting method should satisfy these tests. They are written out
        fully for the sake of clarity'''
        print('testing',sorting_class.__repr__())
        
        no_elements = 500
        
        #sort sparsely spaced random integers
        l = [random.randint(-10000,10000) for i in range(no_elements)]
        self.assertEqual(sorted(l), sorting_class.sort(l))
        
        #sort densely spaced random integers
        l = [random.randint(-100,100) for i in range(no_elements)]
        self.assertEqual(sorted(l), sorting_class.sort(l))
        
        #sort 500 densely spaced random flaots
        l = [random.random() for i in range(no_elements)]
        self.assertEqual(sorted(l), sorting_class.sort(l))
        
        #sort 500 densely spaced random characters
        l = [chr(random.randint(97, 97+25)) for i in range(no_elements)]
        self.assertEqual(sorted(l), sorting_class.sort(l))
        
        #check that classes that don't implement __lt__ can't be sorted
        
        #slightly unusual behaviour for insertion sort and other methods using
        #binary searches - equality check returns first for objects of the same type
        #so a list of anything?(not 100% sure) should return the list that was inputted.
        #this cannot really be considered an error although it is not desirable either
        #in that to sort something, there should be a partial ordering relation defined on the 
        #type of thing that we are sorting. i.e. a<b should either evaluate to true or false
        #for all a,b possible
        l = [math.sin for i in range(int(no_elements/2))] + [math.cos for i in range(int(no_elements/2))]
        with self.assertRaises(TypeError) as type_error_exception:
            sorting_class.sort(l)
            print(type_error_exception.msg)
    
    def test_mergesort(self):
        x = MergeSort(False)
        self.helper_sorting_method(x)
        
      
    def test_bubblesort(self):
        x = BubbleSort(False)
        self.helper_sorting_method(x)
        
    def test_bubblesort_recursive(self):
        x=BubbleSortRecursive(False)
        self.helper_sorting_method(x)
        
    def test_mergesort_recursive(self):
        x = MergeSortRecursive(False)
        self.helper_sorting_method(x)
        
    def test_insertionsort(self):
        x = InsertionSort(False)
        self.helper_sorting_method(x)
        
    def test_quicksort(self):
        x = QuickSort(False)
        self.helper_sorting_method(x)
        
    def test_merge(self):
        ll = sorted([random.randint(-1000,1000) for i in range(50)])
        rl = sorted([random.randint(-1000,1000) for i in range(50)])
        self.assertEqual(sorted(ll+rl), SortingBase.merge(ll,rl))
        

        
    def test_binary_search(self):
        '''Tests the binary search message to ensure an element can be found in a sorted list
        or that it can be inserted in the correct position'''
        l = [1,2,3,5,6]
        element = 4
        self.assertEqual(-4, SortingBase.binary_search(l, element))
        l=[4,6,8,9,12,14,15]
        element = 15
        self.assertEqual(6, SortingBase.binary_search(l, element))
        
        l=[4,6,8,9,12,14,14,14,15]
        element = 7
        self.assertEqual(-(2+1), SortingBase.binary_search(l, element))
        
        l=[4,6,8,9,12,14,14,14,15]
        element = 13
        self.assertEqual(-(5+1), SortingBase.binary_search(l, element))
        
        l=[4,6,8,9,12,14,14,14,15]
        element = 14
        self.assertIn(SortingBase.binary_search(l, element),[5,6,7])
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
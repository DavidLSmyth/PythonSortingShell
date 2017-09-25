# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:02:05 2017

@author: 13383861
"""
#stdlib imports
import unittest
import random
import math
import ctypes

#3rd party imports

#User defined imports
from SortingBase import SortingBase
from SortingClasses import (MergeSort, MergeSortRecursive, BubbleSort, BubbleSortRecursive, 
InsertionSort, QuickSort, CInsertionSort, CBubbleSort, CMergeSort)

class TestSortingClasses(unittest.TestCase):
    
    def c_helper_sorting_method(self, sorting_class):
        '''C wrapper sorting methods should satisfy these tests. They are written out
        fully for the sake of clarity'''
        print('testing',sorting_class.__repr__())
        
        no_elements = 2500
        
        #sort sparsely spaced random integers
        l = [random.randint(-10000,10000) for i in range(no_elements)]
        l_copy = l.copy()
        #must do this since c sorting is in-place
        l_copy=sorting_class.sort(l_copy)
        self.assertEqual(sorted(l), l_copy)
        
        #sort densely spaced random integers
        l = [random.randint(-100,100) for i in range(no_elements)]
        l_copy = l.copy()
        l_copy=sorting_class.sort(l_copy)
        self.assertEqual(sorted(l), l_copy)
    
    def helper_sorting_method(self, sorting_class):
        '''Pure Python sorting method should satisfy these tests. They are written out
        fully for the sake of clarity'''
        print('testing',sorting_class.__repr__())
        
        no_elements = 2500
        
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
            
    def get_source_test_helper(self, sorting_method):
        if isinstance(sorting_method, MergeSort):
            self.assertEqual(sorting_method.get_code().replace(' ','').replace('\n',''),'''def sort(self,iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
                #verify iterable can be sorted
                self._verify_sortable(iterable)
                #lists of length 1 are trivially sorted
                sublists = [iterable[i:i+1] for i in range(0, len(iterable),1)]
                #iterate through each pair of sublists and merge
                while len(sublists)>1:
                    #merging only works if lists have even number of elements
                    if len(sublists)%2:
                        sublists.append([])
                    sublists = list(map(lambda x,y: SortingBase.merge(x,y), sublists[::2], sublists[1::2]))
                return sublists[0]'''.replace(' ','').replace('\n',''))
        else:
            self.assertEqual('','')
    
    def test_mergesort(self):
        '''Ensures that mergesort can sort an iterable successfully'''
        x = MergeSort(False)
        self.helper_sorting_method(x)
        self.get_source_test_helper(x)
      
    def test_bubblesort(self):
        '''Ensures that bubblesort can sort an iterable successfully'''
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
        
    def test_cinsertionsort(self):
        x = CInsertionSort(False)
        self.c_helper_sorting_method(x)
        
    def test_cbubblesort(self):
        x = CBubbleSort(False)
        self.c_helper_sorting_method(x)
    
    def test_cmergesort(self):
        x = CMergeSort(False)
        self.c_helper_sorting_method(x)
        

        
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
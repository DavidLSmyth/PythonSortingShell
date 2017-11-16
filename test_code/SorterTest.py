# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:09:58 2017

@author: 13383861
"""

import unittest
import sys
sys.path.append('..')
from python_files.Sorter import Sorter

class TestSorter(unittest.TestCase):
    
    def setUp(self):
        self.sorter = Sorter()
    
    def test_get_loaded_methods(self):
        self.assertEqual(self.sorter.get_loaded_methods(),[])
        self.sorter.load_all_methods()
        self.assertEqual(self.sorter.get_loaded_methods(), [sorting_method.__name__ for sorting_method in self.sorter._get_available_sorting_methods()])
    
    def test_get_sorting_class(self):
        '''returns the sorting class given it's name'''
        #couldnt figure out error - manually import MergeSort to be sure
        #from python_files.SortingClasses import MergeSort
        self.sorter.load_sorting_method('MergeSort')
        #strange behaviour observed here
        from python_files.SortingClasses import MergeSort
        self.assertEqual(MergeSort.__name__, self.sorter.get_sorting_class('MergeSort').__name__)
        #del MergeSort
        
    def test_get_available_sorting_methods(self):
        self.sorter.load_all_methods()
        self.assertEqual([sorting_method.__name__ for sorting_method in self.sorter._get_available_sorting_methods()], self.sorter.get_loaded_methods())
    
    def test_load_sorting_method(self):
        '''loads class name into current workspace'''
        self.assertEqual(self.sorter.get_loaded_methods(), [])
        self.sorter.load_sorting_method('QuickSort')
        self.assertEqual(self.sorter.get_loaded_methods(), ['QuickSort'])
        self.sorter.load_sorting_method('MergeSort')
        self.assertEqual(set(self.sorter.get_loaded_methods()), {'MergeSort','QuickSort'})
        self.sorter.load_sorting_method('BubbleSort')
        self.assertEqual(set(self.sorter.get_loaded_methods()), {'MergeSort','QuickSort','BubbleSort'})
        #self.sorter.unload_all_loaded_methods()
        
    def test_load_all_methods(self):
        self.sorter.load_all_methods()
        self.assertEqual(self.sorter.get_loaded_methods(), [sorting_method.__name__ for sorting_method in self.sorter._get_available_sorting_methods()])
        
    def test_unload_sorting_method(self):
        '''unloads a single method from the workspace'''
        self.sorter.load_sorting_method('MergeSort')
        self.assertEqual(self.sorter.get_loaded_methods(), ['MergeSort'])
        self.sorter.unload_sorting_method('MergeSort')
        self.assertEqual(self.sorter.get_loaded_methods(), [])
            
    def test_unload_all_loaded_method(self):
        '''unloads all loaded sorting methods from the workspace'''
        self.sorter.load_all_methods()
        self.assertEqual(self.sorter.get_loaded_methods(), [sorting_method.__name__ for sorting_method in self.sorter._get_available_sorting_methods()])
        self.sorter.unload_all_loaded_methods()
        self.assertEqual(self.sorter.get_loaded_methods(), [])
    
    
if __name__ == '__main__':
    unittest.main()
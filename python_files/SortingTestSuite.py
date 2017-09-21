# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:44:34 2017

@author: 13383861
"""

#test suite 


import unittest
from SorterTest import TestSorter
from SortingClassesTest import TestSortingClasses

test_sorter = unittest.TestLoader().loadTestsFromTestCase(TestSorter)
test_sorting_classes = unittest.TestLoader().loadTestsFromTestCase(TestSortingClasses)
testsuite = unittest.TestSuite([test_sorter, test_sorting_classes]) 
unittest.TextTestRunner(verbosity=2).run(testsuite)
#.run(testsuite)


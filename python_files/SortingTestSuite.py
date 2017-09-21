# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:44:34 2017

@author: 13383861
"""

#test suite 

#stdlib
import unittest
import sys

#user defined
from SorterTest import TestSorter
from SortingClassesTest import TestSortingClasses

test_sorter = unittest.TestLoader().loadTestsFromTestCase(TestSorter)
test_sorting_classes = unittest.TestLoader().loadTestsFromTestCase(TestSortingClasses)
test_suite = unittest.TestSuite([test_sorter, test_sorting_classes]) 
runner_result = unittest.TextTestRunner(verbosity=2).run(test_suite).wasSuccessful()
#.run(testsuite)
#ret = not runner.run(test_suite).wasSuccessful()
sys.exit(not runner_result)

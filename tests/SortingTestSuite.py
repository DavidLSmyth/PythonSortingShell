# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:44:34 2017

@author: 13383861
"""

#test suite 

#stdlib
import unittest
import sys
import os
#sys.path.append('../..')
#user defined
print(sys.path)
#explicitly append this to tests so that problems with imports are not encountered
sys.path.append('../python_files')
sys.path.insert(0,os.path.abspath(__file__))
from SortingClassesTest import SortingClassesTest
from SorterTest import TestSorter


def main():
	test_sorter = unittest.TestLoader().loadTestsFromTestCase(TestSorter)
	test_sorting_classes = unittest.TestLoader().loadTestsFromTestCase(SortingClassesTest)
	test_suite = unittest.TestSuite([test_sorter, test_sorting_classes]) 
	runner_result = unittest.TextTestRunner(verbosity=2).run(test_suite).wasSuccessful()
	#.run(testsuite)
	#ret = not runner.run(test_suite).wasSuccessful()
	sys.exit(not runner_result)

if __name__ == '__main__':
	main()
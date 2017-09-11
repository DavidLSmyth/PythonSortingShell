#main sorter class
import sys
import ast
from SortingBase import SortingBase
#from SortingClasses import *
class Sorter:
    def __init__(self):
        pass

    def load_sorting_method(self, sorting_method_name):
        exec('from SortingClasses import {}'.format(sorting_method_name))

    def sort_python(self,list_to_sort, method, element_type = None):
        pass

    def sort_cpp(self,list_to_sort, method, element_type = None):
        pass
    
    def get_available_sorting_methods(self) -> 'dict {sorting_method_repr: class}':
        return{sorting_class.__name__:sorting_class for sorting_class in SortingBase.__subclasses__()}

    def profile_sorting_methods(self):
        pass
        

x = Sorter()
x.load_sorting_method('QuickSort')
x.get_available_sorting_methods()

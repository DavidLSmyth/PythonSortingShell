#base imports
import sys
import ast
import inspect
import collections
import random
from statistics import mean

#3rd party
import numpy as np
import matplotlib.pyplot as plt

#user defined modules
import SortingBase

#from SortingClasses import *
class Sorter:
    def __init__(self):
        self._loaded_sorting_methods = []

    def load_sorting_method(self, sorting_method_name):
        '''loads class name into current workspace'''
        #check whether name has already been loaded
        print('global {}'.format(sorting_method_name),'from SortingClasses import {}'.format(sorting_method_name,sorting_method_name ))
        exec('global {}'.format(sorting_method_name))
        exec('from SortingClasses import {}'.format(sorting_method_name,sorting_method_name ))
        print('Loaded {} into workspace'.format(sorting_method_name))
        self._loaded_sorting_methods.append(eval(sorting_method_name))


    def sort_python(self,iterable: collections.Iterable, sorting_method):
        if(sorting_method in self._loaded_sorting_methods):
            raise Exception('Method not yet loaded')
        else:
            return sorting_method.sort(iterable)

    def sort_cpp(self,list_to_sort, method, element_type = None):
        pass
    
    def get_available_sorting_methods(self) -> 'dict {sorting_method_repr: class}':
        return[sorting_class for sorting_class in SortingBase.SortingBase.__subclasses__()]

    def _get_average_runtime(self,sorting_method,iterable_type = int, input_size = 50):
        '''For a given number of elements, gets the average runtime for 10 runs with that input size'''
        if iterable_type not in [int, float, str]:
            print('Might not be able to generate random types in iterable for {}'.format(sorting_method))
        if iterable_type == int:
            generator = random.randint
            intrange = [-100_000_000,100_000_000]
        elif iterable_type == float:
            generator = lambda start,end: int(random.randint(start,end)*100_000_000)
            intrange = [-100_000_000,100_000_000]
        elif iterable_type == str:
            generator = lambda x: chr(random.randint())
            intrange = [97,122]
        return mean([sorting_method.sort(iterable)[1] for iterable in [[generator(*intrange) for element in range(input_size)]]for l in range(5)])
    
    def profile_sorting_methods(self, all_methods = False):
        '''Runs specified sorting methods on different sized inputs and offers a summary 
        of the runtimes of each.'''
        #maybe use yield here because it takes a while!
        test_sizes = [int((100*i)) for i in range(20,60,4)]
        sorting_method_runtimes = {}
        if all_methods:
            for sorting_class in self.get_available_sorting_methods():
                print('profiling: {}'.format(sorting_class.__name__))
                self.load_sorting_method(sorting_class.__name__)
                sorting_method_runtimes[sorting_class.__name__] = list(map(lambda x: self._get_average_runtime(sorting_class(True), input_size = x), test_sizes))
                
        else:
            for sorting_class in self._loaded_sorting_methods:
                print('profiling: {}'.format(sorting_class.__name__))
                sorting_method_runtimes[sorting_class.__name__] = list(map(lambda x: self._get_average_runtime(sorting_class(True), input_size = x), test_sizes))
        return (test_sizes,sorting_method_runtimes)
        

x = Sorter()
x.load_sorting_method('QuickSort')
x.load_sorting_method('MergeSort')
#x.load_sorting_method('BubbleSort')
x.load_sorting_method('InsertionSort')
print(x.get_available_sorting_methods())
#list(x.get_available_sorting_methods().values())[0]().sort(['a','b','c','z','f'])
times = x.profile_sorting_methods(all_methods=False)
xs = times[0]
ys = list(times[1].values())
labels = list(times[1].keys())
for y,label_name in zip(ys, labels):
    print(y,label_name)
    plt.plot(xs, y,'p-',label = label_name)
#plt.plot(xs, ys[0],'p-', label = labels[0])
#plt.plot(xs, ys[1],'p-',label = labels[1])
#plt.plot(xs, ys[2],'p-',label = labels[2])
plt.legend(loc = 'upper left')
plt.ylabel('Time in milliseconds to run')
plt.xlabel('Size of input')


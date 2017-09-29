#stdlib imports
import collections
import random
from statistics import mean

#3rd party
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D


#user defined modules
import python_files.SortingBase


class Sorter:
    '''A class which can load and unload sorting classes from SortingClasses into the workspace. 
    Methods exist which can then benchmark loaded sorting classes against each other'''
    def __init__(self):
        self._loaded_sorting_methods = []
        
    def get_loaded_methods(self):
        '''Returns the names of the sorting methods that have been loaded into the workspace'''
        return(list(map(lambda x: x.__name__, self._loaded_sorting_methods)))
    
    def get_sorting_class(self,sorting_method_name):
        '''returns the sorting class given it's name'''
        return_class = list(filter(lambda x: x.__name__ == sorting_method_name, self._loaded_sorting_methods))
        if len(return_class)>0:
            return(return_class[0])
        else:
            raise ImportError('Please import {} first'.format(sorting_method_name))

    def load_sorting_method(self, sorting_method_name):
        '''loads class name into current workspace'''
        #check whether name has already been loaded
        if sorting_method_name not in list(map(lambda x: x.__name__,self._loaded_sorting_methods)):
            try:
                exec('global {}'.format(sorting_method_name))
                exec('from python_files.SortingClasses import {}'.format(sorting_method_name,sorting_method_name ))
                print('Loaded {} into current workspace'.format(sorting_method_name))
                self._loaded_sorting_methods.append(eval(sorting_method_name))
            except ImportError as e:
                print('Could not load {} into the workspace'.format(sorting_method_name))
        else:
            print('{} has already been loaded into the workspace'.format(sorting_method_name))
        
    def load_all_methods(self):
        for sorting_method in self._get_available_sorting_methods():
            self.load_sorting_method(sorting_method.__name__)
            
    def load_c_methods(self):
        for sorting_method in self._get_available_sorting_methods():
            if(sorting_method.__name__[0] == 'C'):
                self.load_sorting_method(sorting_method.__name__)
        
    def unload_sorting_method(self, sorting_method_name):
        '''unloads a single method from the workspace'''
        if sorting_method_name in self.get_loaded_methods():
            self._loaded_sorting_methods.remove(self.get_sorting_class(sorting_method_name))
            #del list(filter(lambda x: x.__name__ == sorting_method_name, self._loaded_sorting_methods))[0]
            #don't need to remove this from the list as it's already been removed from the workspace
            print('unloaded {} from the workspace'.format(sorting_method_name))
        else:
            print('{} was not loaded: cannot remove'.format(sorting_method_name))
            
    def unload_all_loaded_methods(self):
        '''unloads all loaded sorting methods from the workspace'''
        for sorting_method in self._get_available_sorting_methods():
            self.unload_sorting_method(sorting_method.__name__)

    def sort_python(self,iterable: collections.Iterable, sorting_method):
        if(sorting_method in self._loaded_sorting_methods):
            raise Exception('Method not yet loaded')
        else:
            return sorting_method.sort(iterable)

    def sort_c(self,iterable: collections.Iterable, sorting_method, element_type = None):
        if(sorting_method in self._loaded_sorting_methods):
            raise Exception('Method not yet loaded')
        else:
            return sorting_method.sort(iterable)
    
    def _get_available_sorting_methods(self) -> 'dict {sorting_method_repr: class}':
        return[sorting_class for sorting_class in python_files.SortingBase.SortingBase.__subclasses__()]

    def _get_average_runtime(self,sorting_method,iterable_type = int, input_size = 50, no_runs = 1):
        '''For a given number of elements, gets the average runtime for 3 runs with that input size'''
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
        return mean([sorting_method.sort(iterable)[1] for iterable in [[generator(*intrange) for element in range(input_size)]]for l in range(no_runs)])
    
    def profile_sorting_methods(self, all_methods = False):
        '''Runs specified sorting methods on different sized inputs and offers a summary 
        of the runtimes of each.'''
        print('\nProfiling loaded sorting methods. This may take a while...\n')
        #maybe use yield here because it takes a while!
        test_sizes = [int((100*i)) for i in range(20,80,4)]
        sorting_method_runtimes = {}
        if all_methods:
            #make a copy of currently loaded methods
            currently_loaded_methods = self._loaded_sorting_methods
            self.load_all_methods()
                
        for sorting_class in self._loaded_sorting_methods:
            print('profiling: {}'.format(sorting_class.__name__))
            sorting_method_runtimes[sorting_class.__name__] = list(map(lambda x: self._get_average_runtime(sorting_class(True), input_size = x), test_sizes))
        if all_methods:
            for method_to_unload in list(filter(lambda x: x not in currently_loaded_methods, self._loaded_sorting_methods)):
                self.unload_sorting_method(method_to_unload.__name__)
        return (test_sizes,sorting_method_runtimes)
    
    def plot_timings(self, all_methods = False, save_file_name = False, ThreeD = False):
        test_sizes, sorting_method_runtimes = self.profile_sorting_methods(all_methods)    
        plt.clf()
        if not ThreeD:
            for runtime, label_name in zip(list(sorting_method_runtimes.values()), list(sorting_method_runtimes.keys())):
                plt.plot(test_sizes, runtime,'p-',label = label_name)
            plt.ylabel('Time in milliseconds to run')
            plt.xlabel('Size of input')

        else:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(111, projection='3d')
            #(runtime, label_name) 
            for index, runtime, label_name in zip([i for i in range(len(sorting_method_runtimes.values()))],list(sorting_method_runtimes.values()), list(sorting_method_runtimes.keys())):
                self.ax.plot(test_sizes,[index for i in range(len(runtime))],runtime,'p-', label = label_name)
            self.ax.set_xlabel('Size of input')
            self.ax.set_ylabel('Sorting Algo')
            self.ax.set_zlabel('Time in milliseconds to run')
            #[index for i in range(len(runtime))], 
            self.ax.set_yticklabels(list(sorting_method_runtimes.keys()))
                
        plt.legend(loc = 'upper left')

        if save_file_name:
            import os
            os.chdir('.')
            plt.savefig(f'../{save_file_name}.png')
            

            
        

#x = Sorter()
#x.load_sorting_method('QuickSort')
#x.load_sorting_method('MergeSort')
#x.load_all_methods()
#x.unload_sorting_method('BubbleSortRecursive')
#x.unload_sorting_method('MergeSortRecursive')
#x._get_available_sorting_methods()
#x.get_loaded_methods()
#x.unload_sorting_method('QuickSort')
#x.get_loaded_methods()
#x._loaded_sorting_methods
#x.plot_timings()





##x.load_sorting_method('BubbleSort')
#x.load_sorting_method('InsertionSort')
#print(x._get_available_sorting_methods())
##list(x.get_available_sorting_methods().values())[0]().sort(['a','b','c','z','f'])
#times = x.profile_sorting_methods(all_methods=False)
#xs = times[0]
#ys = list(times[1].values())
#labels = list(times[1].keys())
#for y,label_name in zip(ys, labels):
#    print(y,label_name)
#    plt.plot(xs, y,'p-',label = label_name)
##plt.plot(xs, ys[0],'p-', label = labels[0])
##plt.plot(xs, ys[1],'p-',label = labels[1])
##plt.plot(xs, ys[2],'p-',label = labels[2])
#plt.legend(loc = 'upper left')
#plt.ylabel('Time in milliseconds to run')
#plt.xlabel('Size of input')


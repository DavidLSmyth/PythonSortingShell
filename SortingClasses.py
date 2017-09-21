#a file which contains sorting functions which are called by a Sorter class
#To add a sorting function, ensure that the function signature is
#list = [], type = []

#stdlib
import collections
from random import randint


#3rd party

#user defined
from SortingMeta import SortingMeta
from SortingBase import SortingBase
from CFunctionMixin import CFunctionMixin 




class BubbleSort(SortingBase,metaclass=SortingMeta):
    
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'Bubble Sort'
    
    def sort(self,iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
        #verify iterable can be sorted
        self._verify_sortable(iterable)
        for sorted_elements_index in range(len(iterable),0,-1):
            for unsorted_elements_index in range(len(iterable[:sorted_elements_index])-1):
                if iterable[unsorted_elements_index]>iterable[unsorted_elements_index+1]:
                    #swap with next
                   iterable[unsorted_elements_index], iterable[unsorted_elements_index+1] = iterable[unsorted_elements_index+1], iterable[unsorted_elements_index]
        return iterable
    
class BubbleSortRecursive(SortingBase,metaclass=SortingMeta):
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'Bubble Sort Recursive'

    def sort(self,iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
        self._verify_sortable(iterable)
        import sys
        sys.setrecursionlimit(100000)
        #move recursive work to separate function to preserve timing
        return(self.sort_recursive(iterable))
        
    def sort_recursive(self,iterable: collections.Iterable, no_iterations = 0):
        #on each iteration, one element moves to correct position in list
        if no_iterations == len(iterable)-1:
            print('Sorted in ', no_iterations, ' iterations')
            return(iterable)
        else:
            #move the recursive work to another function to preserve decorator timing
            for unsorted_elements_index in range(len(iterable[:-no_iterations-1])):
                if iterable[unsorted_elements_index]>iterable[unsorted_elements_index+1]:
                    #swap with next
                   iterable[unsorted_elements_index], iterable[unsorted_elements_index+1] = iterable[unsorted_elements_index+1], iterable[unsorted_elements_index] 
            return(self.sort_recursive(iterable, no_iterations+1))


class MergeSort(SortingBase,metaclass=SortingMeta):
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'Merge Sort'
    
    def sort(self,iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
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
        return sublists[0]

class MergeSortRecursive(SortingBase, metaclass = SortingMeta):
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'Recursive Merge Sort'
        
    def sort(self, iterable: collections.Iterable)->'tuple(iterable, int) if timed else iterable':
        #verify iterable can be sorted
        self._verify_sortable(iterable)
        
        if len(iterable)==1:
            return iterable
        else:
            return(SortingBase.merge(self.sort(iterable[:int(len(iterable)/2)]), self.sort(iterable[int(len(iterable)/2):])))
        

class QuickSort(SortingBase, metaclass = SortingMeta):
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'Quick Sort'
        
    def sort(self, iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
        '''Sorts a list in-place. Procedure: 
            While not sorted: 
                pick a random element that has not been sorted. 
        '''
        return self.sort_recursive(iterable)
        
    def sort_recursive(self,iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
        #print('iterable',iterable)
        if len(iterable)==0:
            return []
        elif len(iterable) == 1:
            return iterable 
        else:
            wall_index = randint(0, len(iterable)-1)
           # print('wall_index, wall: {}, {}'.format(wall_index, iterable[wall_index]))
            return self.sort_recursive(list(filter(lambda x: x<iterable[wall_index], iterable))) + list(filter(lambda x: x==iterable[wall_index], iterable)) + self.sort_recursive(list((filter(lambda x: x>iterable[wall_index], iterable))))
    
class InsertionSort(SortingBase, metaclass = SortingMeta):   
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'Insertion Sort'
        
    def sort(self, iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
        '''Begin with an empty list. Insert element by element to sorted list'''
        #future implementation - pop each element off iterable and insert it in the sorted list
        sorted_list = [iterable[0]]
        for element in iterable[1:]:
            position=SortingBase.binary_search(sorted_list,element)
            if position>=0:
                sorted_list.insert(position, element)
            else:
                sorted_list.insert(-(position+1),element)
        return sorted_list
    
#Maybe mixin is not really necessary here. 
#In python, inheritance order is from right to left
class CInsertionSort(CFunctionMixin,SortingBase, metaclass = SortingMeta):
    '''A c implementation of insertion sort. The sorting method is simply a 
    wrapper for a c function that sorts a list in-place'''
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'c_insertion_sort'
    
    def sort(self, iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
        '''Begin with an empty list. Insert element by element to sorted list'''
        return super().sort(iterable)

    
class CBubbleSort(CFunctionMixin,SortingBase, metaclass = SortingMeta):
    '''A c implementation of bubble sort. The sorting method is simply a 
    wrapper for a c function that sorts a list in-place'''
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'c_bubble_sort'
    
    def sort(self, iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
        '''Begin with an empty list. Insert element by element to sorted list'''
        return super().sort(iterable)
    
class CMergeSort(CFunctionMixin,SortingBase, metaclass = SortingMeta):
    '''A c implementation of merge sort. The sorting method is simply a 
    wrapper for a c function that sorts a list in-place'''
    def __init__(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'c_merge_sort'
    
    def sort(self, iterable):
        return super().sort(iterable)
    
#    def sort(self, iterable: collections.Iterable) -> 'tuple(iterable, int) if timed else iterable':
#        '''Begin with an empty list. Insert element by element to sorted list'''
#        sorting_method = self.load_c_function(self.__repr__())
#        c_iterable = self.prepare_c_int_array(iterable)
#        sorting_method(c_iterable, len(c_iterable))
#        return list(c_iterable)      
    

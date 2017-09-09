#a file which contains sorting functions which are called by a Sorter class
#To add a sorting function, ensure that the function signature is
#list = [], type = []

#stdlib
import collections

#3rd party

#user defined
from SortingMeta import SortingMeta
from SortingBase import SortingBase




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
            sublists = list(map(lambda x,y: self.merge(x,y), sublists[::2], sublists[1::2]))
        return sublists[0]

class MergeSortRecursive(SortingBase, metaclass = SortingMeta):
    def __init(self, timed = True):
        super().__init__(timed)
        
    def __repr__(self):
        return 'Recursive Merge Sort'
        
    def sort(self, iterable: collections.Iterable)->'tuple(iterable, int) if timed else iterable':
        #verify iterable can be sorted
        self._verify_sortable(iterable)
        
        if len(iterable)==1:
            return iterable
        else:
            return(self.merge(self.sort(iterable[:int(len(iterable)/2)]), self.sort(iterable[int(len(iterable)/2):])))
        

class QuickSort(SortingBase, metaclass = SortingMeta):
    def sort(self, iterable: collections.Iterable):
        pass

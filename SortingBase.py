# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:55:25 2017

@author: 13383861
"""
import collections
import time
def timer(function):
    def wrapper(*args, **kwargs):
        '''Given a list_to_sort of type element_type, returns the sorted list
        Args:
        iterable: A list of elements of a given type
        Returns:
        if self.timed: 
            tuple(iterable ordered descending, time taken to sort)
        else:
            iterable ordered descending
        '''
        start = time.time()
        result = function(*args, **kwargs)
        finish = time.time()
        print('Function took {} ms to run'.format((finish-start)*1000))
        return result, (finish-start)*1000
    return wrapper


        

class SortingBase:
    def __init__(self, timed):
        self.timed = timed
        #if the function is to be timed, use the wrapper
        if self.timed:
            self.sort = timer(self.sort)
            
    #should be able to merge two lists even if class is not instantiated
    #this is really an auxiliary method and should probably go in its own file...
    @classmethod
    def merge(self,ll,rl):
        '''merges two sorted lists, ll and rl to give a sorted list. Auxiliary method used in multiple derived classes'''
        merged_list = []
        counter_l=0
        counter_r=0
        #print('merging {} and {}'.format(ll,rl))
        while counter_l!=len(ll) or counter_r!=len(rl):
            if counter_l==len(ll):
                #since l2 is sorted, just append it on
                merged_list.extend(rl[counter_r:])
                return merged_list
            
            elif counter_r==len(rl):
                merged_list.extend(ll[counter_l:])
                return merged_list
            
            else:
                if ll[counter_l] < rl[counter_r]:
                    merged_list.append(ll[counter_l])
                    counter_l+=1
                else:
                    merged_list.append(rl[counter_r])
                    counter_r+=1            
        return merged_list
     
    @classmethod
    def binary_search(self, iterable:'ordered collections.Iterable', element: 'Element of same type of l', position_to_insert = 0) -> 'Position in list or position to insert if nor present in list':
        '''Searches an iterable for a given element. If found, returns position in iterable. If not found, returns
        position to insert'''
        #ToDo: verify that iterable is sorted
        #print('iterable: ',iterable,'position_to_insert',position_to_insert)
        if len(iterable) == 0:
            #have checked every possibel position, not located in list
            #return where should be inserted
            return -(position_to_insert+1)
        elif element == iterable[int(len(iterable)/2)]:
            return position_to_insert + int(len(iterable)/2)
        elif element > iterable[int(len(iterable)/2)]:
            return self.binary_search(iterable[int(len(iterable)/2)+1:], element, position_to_insert+int(len(iterable)/2)+1)
        else: 
            return self.binary_search(iterable[:int(len(iterable)/2)], element, position_to_insert)
            
        
    #override in subclasses. This gives common docstring if not defined in subclasses
    def sort(self, iterable: collections.Iterable):
        '''Given a list_to_sort of type element_type, returns the sorted list
        Args:
        iterable: A list of elements of a given type
        Returns:
        if self.timed: 
            tuple(iterable ordered descending, time taken to sort)
        else:
            iterable ordered descending
        '''
        pass
            
    def __is_iterable(self,iterable: collections.Iterable):
        if isinstance(iterable, collections.Iterable):
            #print('object is iterable')
            return True
        else:
            #return False
            return TypeError('Can only sort iterable data structure')

    
    def __iterable_type_uniform(self,iterable: collections.Iterable):
        datatype = type(iterable[0])
        if all(map(lambda x: isinstance(x,datatype), iterable)) and hasattr(iterable[0],'__gt__'):
            #print('iterable is all of a consistent type')
            return True
        else:
            #print('iterable is not consistent type')
            return TypeError('Iterable is not of a consistent type. Expecting type {}'.format(datatype))
        
    def __implements_lt(self, iterable: collections.Iterable):
        pass
        
    def _verify_sortable(self,iterable):
        '''Ensures that object is actually sortable. If object is not sortable, returns list of TypeError.
        Unsortable list is detected before sorting has begun'''
        #Raise all exceptions
        for i in list(filter(lambda x: isinstance(x, Exception),map(lambda f: f(iterable),[self.__is_iterable, self.__iterable_type_uniform, self.__implements_lt]))):
            raise i
       
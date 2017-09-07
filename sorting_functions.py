#a file which contains sorting functions which are called by a Sorter class
#To add a sorting function, ensure that the function signature is
#list = [], type = []
def sorting_verifier(list_to_sort):
    '''Verifies that list can be sorted'''
    #allow sub types as well?
    element_type = type(list_to_sort[0])
    #ensure that each element is the same type as the first give element
    return(all(isinstance(x,element_type) for x in list_to_sort))
               
def bubble_sort(list_to_sort:list = []) -> list:
    '''Given a list_to_sort of type element_type, returns the sorted list
    Args:
        list_to_sort: A list of elements of a given type
        param2: The type of each element in list_to_sort
    Returns:
        list_to_sort in descending order
    '''
    #infer type based on first element
    if not sorting_verifier(list_to_sort):
       #cannot be sorted
        print('list cannot be sorted')

    else:
           #elements in list are all of the same
        for sorted_elements_index in range(len(list_to_sort),0,-1):
            for unsorted_elements_index in range(len(list_to_sort[:sorted_elements_index])-1):
                if list_to_sort[unsorted_elements_index]>list_to_sort[unsorted_elements_index+1]:
                    #swap with next
                   list_to_sort[unsorted_elements_index], list_to_sort[unsorted_elements_index+1] = list_to_sort[unsorted_elements_index+1], list_to_sort[unsorted_elements_index]
                print(list_to_sort)
        return list_to_sort

def bubble_sort_recursive(list_to_sort: list = [], no_iterations = 0)->list:
    #on each iteration, one element moves to correct position in list
    if not sorting_verifier(list_to_sort):
        print('Elements cannot be compared - unable to sort')
    if no_iterations == len(list_to_sort)-1:
        print('Sorted in ', no_iterations, ' iterations')
        return(list_to_sort)
    else:
        for unsorted_elements_index in range(len(list_to_sort[:-no_iterations-1])):
            if list_to_sort[unsorted_elements_index]>list_to_sort[unsorted_elements_index+1]:
                #swap with next
               list_to_sort[unsorted_elements_index], list_to_sort[unsorted_elements_index+1] = list_to_sort[unsorted_elements_index+1], list_to_sort[unsorted_elements_index] 
        return(bubble_sort_recursive(list_to_sort, no_iterations+1))

def merge_sort(list_to_sort: list = [])->list:
    pass
#print(bubble_sort([1,2,7,5,8]))
print(bubble_sort_recursive([1,2,7,5,3]))

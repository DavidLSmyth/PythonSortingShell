from multiprocessing import Pool
 
def doubler(number):
	return number * 2
 
def mergesort1(l):
	if len(l) <= 1:
		return l
	else:
		return merge(mergesort(l[:int(len(l)/2)]), mergesort(l[int(len(l)/2):]))
 
    
def merge(ll,rl):
    '''Merges two sorted lists, ll and rl to give a sorted list. Auxiliary method used in multiple derived classes'''
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

def parallel_merge(l):
	'''Merges two sorted lists, ll and rl to give a sorted list. Auxiliary method used in multiple derived classes'''
	merged_list = []
	ll = l[:int(len(l)/2)]
	rl = l[int(len(l)/2):]
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
	
def parallel_merge_in_place(l, ll_start_index, mid_index, rl_end_index):
	'''Merges two sorted lists, ll and rl to give a sorted list. Auxiliary method used in multiple derived classes'''
	merged_list = []
	ll = l[ll_start_index:mid_index]
	rl = l[mid_index:rl_end_index]
	counter_l=0
	counter_r=0
	counter_current = ll_start
	no_els_to_sort_ll = mid_index - ll_start_index
	no_els_to_sort_rl = rl_end_index - mid_index
	#print('merging {} and {}'.format(ll,rl))
	while counter_l != no_els_to_sort_ll or counter_r!=no_els_to_sort_rl:
		if counter_l==no_els_to_sort_ll:
			#since l2 is sorted, just append it on
			merged_list.extend(rl[counter_r:])
			l[ll_start_index:rl_end_index] = l
			return
			#return merged_list
		
		elif counter_r==no_els_to_sort_rl:
			merged_list.extend(ll[counter_l:])
			l[ll_start_index:rl_end_index] = l
			#return merged_list
			return
		
		else:
			if ll[counter_l] < rl[counter_r]:
				merged_list.append(ll[counter_l])
				counter_l+=1
			else:
				merged_list.append(rl[counter_r])
				counter_r+=1            
	return #merged_list
	
	
def parallel_merge_in_place(l, ll_start_index, mid_index, rl_end_index):
	'''Merges two sorted lists, ll and rl to give a sorted list. Auxiliary method used in multiple derived classes'''
	merged_list = []
	ll = l[ll_start_index:mid_index]
	rl = l[mid_index:rl_end_index]
	if not rl: 
		return ll
	counter_l=0
	counter_r=0
	#counter_current = ll_start_index
	no_els_to_sort_ll = mid_index - ll_start_index
	no_els_to_sort_rl = rl_end_index - mid_index
	print('merging {} and {}'.format(ll,rl))
	while counter_l != no_els_to_sort_ll or counter_r!=no_els_to_sort_rl:
		if counter_l==no_els_to_sort_ll:
			#since l2 is sorted, just append it on
			merged_list.extend(rl[counter_r:])
			l[ll_start_index:rl_end_index] = merged_list
			print('merged list')
			print(merged_list)
			print('l')
			print(l)
			return merged_list
			#return merged_list
		
		elif counter_r==no_els_to_sort_rl:
			merged_list.extend(ll[counter_l:])
			l[ll_start_index:rl_end_index] = merged_list
			#return merged_list
			print('merged list')
			print(merged_list)
			print('l')
			print(l)
			return merged_list
		
		else:
			if ll[counter_l] < rl[counter_r]:
				merged_list.append(ll[counter_l])
				counter_l+=1
			else:
				merged_list.append(rl[counter_r])
				counter_r+=1            
	return merged_list

#to_merge = [1,4,2,66,6,8,34,5,6,10]
#print(to_merge)
#parallel_merge_in_place(to_merge, 2, 4, 6)
#print(to_merge)
#assert(to_merge == [1,4,2,6,8,66,34,5,6,10])
def product_helper(args):
	return parallel_merge_in_place(*args)


	
	
	
	
from multiprocessing import Pool
import functools




def mergesort(l: list) -> list:
	if len(l) <=1:
		return l
	else:
		gallop = 0
		while 2**gallop<=len(l):
			#parallelise this if overhead is small
			merge_indices = [[l, i, i+2**gallop, i+2**(gallop+1)] for i in range(0, len(l), 2**(gallop+1))]
			if len(l) > 1024:
				#print('merge indices: ', merge_indices)
				l = functools.reduce(lambda x,y: x + y, pool.map_async(helper, merge_indices).get())
			else:
				l = functools.reduce(lambda x,y: x + y, [helper(merge_index) for merge_index in merge_indices])
            
            #for i in range(0,len(l), 2**gallop):
             #   print(i)
              #  print('{}:{}'.format(i,i+(2**gallop)))
               # print('')
                #print(l)
                #each of these can be performed in parallel
#                merge(l[i:i+(2**int(gallop/2)], l[i+(2**int(gallop)/2):i+(i**int(gallop/2))])
                #l[i:i+(2**gallop)] = merge(l[i:i+int((2**gallop)/2)], l[i+int(2**(gallop)/2):i+int(2**(gallop))])
#                l[i:i+(2**gallop)]
#print(l)
			gallop += 1
		#final merge
		return merge(l[:int((2**gallop)/2)], l[int((2**gallop)/2):])
        
def parallel_merge_in_place(l, ll_start_index, mid_index, rl_end_index):
	'''Merges two sorted lists, ll and rl to give a sorted list. Auxiliary method used in multiple derived classes'''
	rl_end_index = rl_end_index if rl_end_index < len(l) else len(l)
	merged_list = []
	ll = l[ll_start_index:mid_index]
	rl = l[mid_index:rl_end_index]
	if not rl: 
		return ll
	counter_l=0
	counter_r=0
	#counter_current = ll_start_index
	no_els_to_sort_ll = mid_index - ll_start_index
	no_els_to_sort_rl = rl_end_index - mid_index
	#print('merging {} and {}'.format(ll,rl))
	while counter_l != no_els_to_sort_ll or counter_r!=no_els_to_sort_rl:
		if counter_l==no_els_to_sort_ll:
			#since l2 is sorted, just append it on
			merged_list.extend(rl[counter_r:])
			l[ll_start_index:rl_end_index] = merged_list
			#print('merged list')
			#print(merged_list)
			#print('l')
			#print(l)
			return merged_list
			#return merged_list
		
		elif counter_r==no_els_to_sort_rl:
			merged_list.extend(ll[counter_l:])
			l[ll_start_index:rl_end_index] = merged_list
			#return merged_list
			#print('merged list')
			#print(merged_list)
			#print('l')
			#print(l)
			return merged_list
		
		else:
			if ll[counter_l] < rl[counter_r]:
				merged_list.append(ll[counter_l])
				counter_l+=1
			else:
				merged_list.append(rl[counter_r])
				counter_r+=1            
	return merged_list
    
def helper(args):
	return parallel_merge_in_place(*args)	
import random
import functools
import time	
if __name__ == '__main__':
	to_sort = [random.random() for i in range(50000)]
	pool = Pool(processes=16)
	#merge_indices = [[to_sort, i, i+2, i+4] for i in range(0, len(to_sort), 4)]
	#print('merge indices: ')
	#print(merge_indices)
	#pool = Pool(processes=4)
	#print(help(pool.map))
	#res = functools.reduce(lambda x,y: x + y, pool.map_async(product_helper, merge_indices).get())
	#print('res1', res)
	#merge_indices = [[res, i, i+4, i+8] for i in range(0, len(res), 8)]
	#res = functools.reduce(lambda x,y: x + y, pool.map_async(product_helper, merge_indices).get())
	#print('res2', res)
	#pool.map_async(merge(
	t = time.time()
	assert(mergesort(to_sort) == sorted(to_sort))
	t1 =  time.time() - t
	print('\n', t1)
	
	t = time.time()
	assert(mergesort1(to_sort) == sorted(to_sort))
	t2 =  time.time() - t
	print('\n', t2)
	
	t = time.time()
	sorted(to_sort)
	t3 = time.time() - t
	print('\n', t3)
	print(t1/t3)
	print(t1/t2)
	
	
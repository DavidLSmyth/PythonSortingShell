#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ctypes
import os
os.chdir('./Dropbox')
test_lib = ctypes.CDLL("./libhello.so")
#sets the return type
test_lib.restype = ctypes.c_int32
#sets the arg types
test_lib.argtypes = [ctypes.c_int32,]
def c_echo(integer):
	if(isinstance(integer, int)):
		return test_lib.simple_function(integer)
	else:
		raise TypeError('type {} is not an integer'.format(type(integer)))

print(c_echo(10))
print(c_echo(15))
#print(c_echo('hi'))

insertionSort = test_lib.insertionSort
my_array_type = ctypes.c_int * 5
my_array = my_array_type()
my_array[0:] = [1,8,6,4,5]
#my_array_type = ctypes.c_int * len(array)
insertionSort.restype = None
insertionSort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
insertionSort(my_array, len(my_array))
print([i for i in my_array])
#ctrl + shift + / to multiline comment
# 16.16.1.6. Calling functions with your own custom data types

# You can also customize ctypes argument conversion to allow instances
 # of your own classes be used as function arguments. ctypes looks for 
 # an _as_parameter_ attribute and uses this as the function argument. 
 # Of course, it must be one of integer, string, or bytes:
# >>>

# >>> class Bottles:
# ...     def __init__(self, number):
# ...         self._as_parameter_ = number
# ...
# >>> bottles = Bottles(42)
# >>> printf(b"%d bottles of beer\n", bottles)
# 42 bottles of beer
# 19
# >>>

#If you don’t want to store the instance’s data in the _as_parameter_ instance
# variable, you could define a property which makes the attribute available on request.

# If you have defined your own classes which you pass to function calls, you have to 
# implement a from_param() class method for them to be able to use them in the argtypes 
# sequence. The from_param() class method receives the Python object passed to the
#  function call, it should do a typecheck or whatever is needed to make sure this object 
#  is acceptable, and then return the object itself, its _as_parameter_ attribute, or
#   whatever you want to pass as the C function argument in this case. Again, the result
#    should be an integer, string, bytes, a ctypes instance, or an object with 
#    an _as_parameter_ attribute.
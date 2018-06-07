# PythonSortingShell ![alt text](https://travis-ci.org/DavidLSmyth/PythonSortingShell.svg?branch=master)
A project which implements various sorting algorithms which can then be benchmarked against each other. Written to practice: 

* Using github to effectively version control the project.
* Investigating python class design with metaclasses, Inheritance, mixins.
* Practice using python to wrap C functions with the ctypes library to give speed boost to python functions (cffi addition would be nice).
* Practice using CI tools such as travis.
* Practice writing sorting algorithms efficiently.

Written and tested using Ubuntu 16.04. Install MinGW on windows with make and gcc in order to run on Windows. Alternatively compile the sorting library to a dll manually (visual studio compiler is probably easiest) and then modify the windows makefile (c_code/MakeFileWin) correspondingly.

## Extending the code to add your own sorting classes written in c to be benchmarked. 
This is a simple process: Define the function you wish to add as c_<sorting function name> in c_code/sorting_functions.h and provide the corresponding implementation in c_code/sorting_functions.c. Currently the code only supports functions that sort integers but extension to other data types should be straightforward. Then add a corresponding python class in SortingClasses.py which extends CFuncionMixin, SortingBase and has metaclass SortingMeta.The following code template is provided as an example (bubble sort chosen as an example):
  
```
class CBubbleSort(CFunctionMixin, SortingBase, metaclass=SortingMeta):
    def __init__(self, timed=True):
        super().__init__(timed)

    def __repr__(self):
        return 'c_bubble_sort'

    def sort(self, iterable: collections.Iterable):
        return super().sort(iterable)
```
## Extending the code to add your own sorting class written in python
Again, this is simple: Define a class that extends SortingBase and has metaclass SortingMeta with a __repr__ method and overridden sort method. In order to benchmark the algorithm, define __init__ as 
```def __init__(self, timed = True):
      super().__init__(timed)
```

## Generating benchmarked figures
Edit and generate_fig.py to generate figures of the runtimes of desired sorting algorithms

## Examples of generated figures:
![alt text](https://github.com/DavidLSmyth/PythonSortingShell/blob/master/demo.png)
![alt text](https://github.com/DavidLSmyth/PythonSortingShell/blob/master/demo1.png)


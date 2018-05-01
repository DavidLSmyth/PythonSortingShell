gcc -c -Wall -Werror -fpic sorting_functions.c
gcc -shared -o libsorting_functions.dll sorting_functions.o

gcc -c -Wall -Werror -fpic sorting_functions.c
gcc -shared -o libsorting_functions.so sorting_functions.o

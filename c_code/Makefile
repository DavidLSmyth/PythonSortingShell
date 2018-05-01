libsorting_functions.so: sorting_functions.o
	gcc -shared -o libsorting_functions.so sorting_functions.o

sorting_functions.o: sorting_functions.c
	gcc -c -Wall -Werror -fpic sorting_functions.c

clean:
	rm sorting_functions.o libsorting_functions.so
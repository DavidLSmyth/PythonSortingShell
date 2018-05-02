#This is a linux makefile for convenience
#Running make will compile the shared libraries necessary for python sorting shell
ifeq ($(OS),Windows_NT)
    DLLEXT := .dll
else
    DLLEXT := .so
endif

DLL := libsorting_functions$(DLLEXT)


#lib : $(DLL)


$(DLL): sorting_functions.o
	@echo $(DLLEXT)
	gcc -shared -o $(DLL) sorting_functions.o


sorting_functions.o: sorting_functions.c
	@echo $(DLL)
	if[ $(DLLEXT) = .so ]; then \
		cp sorting_functions_base.c sorting_functions.c
		sed -e "s/__declspec(dllexport) //g" sorting_functions.c > sorting_functions.c
		gcc -c -Wall -Werror -fpic sorting_functions.c
	else \
		cp sorting_functions_base.c sorting_functions.c
		gcc -c -Wall -Werror -fpic sorting_functions.c
	fi

clean:
	@echo $(DLL)
	if [[ $(DLLEXT) = .so ]] then rm sorting_functions.o libsorting_functions.so
	else del sorting_functions.o libsorting_functions.dll
	fi


#gcc -c -Wall -Werror -fpic sorting_functions.c
#gcc -shared -o libsorting_functions.dll sorting_functions.o
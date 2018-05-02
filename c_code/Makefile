#This is a linux makefile for convenience
#Running make will compile the shared libraries necessary for python sorting shell

#detects the OS
OSFLAG 				:=
ifeq ($(OS),Windows_NT)
	OSFLAG += -D WIN32
	ifeq ($(PROCESSOR_ARCHITECTURE),AMD64)
		OSFLAG += -D AMD64
	endif
	ifeq ($(PROCESSOR_ARCHITECTURE),x86)
		OSFLAG += -D IA32
	endif
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		OSFLAG += -D LINUX
	endif
	ifeq ($(UNAME_S),Darwin)
		OSFLAG += -D OSX
	endif
		UNAME_P := $(shell uname -p)
	ifeq ($(UNAME_P),x86_64)
		OSFLAG += -D AMD64
	endif
		ifneq ($(filter %86,$(UNAME_P)),)
	OSFLAG += -D IA32
		endif
	ifneq ($(filter arm%,$(UNAME_P)),)
		OSFLAG += -D ARM
	endif
endif

all:
	@echo $(OSFLAG)

	
init:
	ifeq ($(OS),Windows_NT)
		@echo "Building c code for windows"
		cp sorting_functions_base.c sorting_functions.c
		gcc -c -Wall -Werror -fpic sorting_functions.c
		gcc -shared -o libsorting_functions.dll sorting_functions.o
	endif
	else
		@echo "Building c code for linux"
		UNAME_S := $(shell uname -s)
		ifeq ($(UNAME_S),Linux)
			cp sorting_functions_base.c sorting_functions.c
			sed -e "s/__declspec(dllexport) //g" sorting_functions_base.c > sorting_functions.c
			gcc -c -Wall -Werror -fpic sorting_functions.c
			gcc -shared -o libsorting_functions.so sorting_functions.o
		endif
	endif


#libsorting_functions.so: sorting_functions.o
#gcc -shared -o libsorting_functions.so sorting_functions.o

#sorting_functions.o: sorting_functions.c
#gcc -c -Wall -Werror -fpic sorting_functions.c

clean:
    ifeq ($(OS),Windows_NT)
		@echo "Building c code for windows"
		del sorting_functions.o libsorting_functions.dll
	endif
	else
		@echo "Building c code for linux"
		UNAME_S := $(shell uname -s)
		ifeq ($(UNAME_S),Linux)
			rm sorting_functions.o libsorting_functions.so
		endif
	endif
endif
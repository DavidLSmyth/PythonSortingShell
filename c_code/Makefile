hello.so: hello.o
	gcc -shared -o libhello.so hello.o

hello.o: hello.c
	gcc -c -Wall -Werror -fpic hello.c
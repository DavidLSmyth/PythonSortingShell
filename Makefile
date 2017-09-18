TestCCode.dll: TestCCode.o
	gcc -m64 -shared -o TestCCode.dll TestCCode.o
TestCCode.o: TestCCode.c
	gcc -m64 -c -Wall -Werror -fpic TestCCode.c
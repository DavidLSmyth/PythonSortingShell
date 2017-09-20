#include <stdio.h>
#include <math.h>
#include <string.h>
#include "sorting_functions.h"

int main(){
	//the size of the array
	int n = 10;
	int array [10] = {9,6,4,3,2,11,16,20, 12, 15};
	int array1[10];
	memcpy(&array1, &array, n*sizeof(int));
	printArray(array, n);
	printf("array1: \n");
	printArray(array1, n);
	swap(& array[2], & array[3]);
	printf("The array with elements 2 and 3 swapped: \n");
	printArray(array,n);
	if((array[2] == 3) & (array[3] == 4)){
		printf("Swap function works as intended!\n");
	} 
	else{
		printf("Swap function has errors\n");
	}
	printf("array1: \n");
	printArray(array1, n);
	bubbleSort(array1, n);
	printf("array1 sorted: \n");
	printArray(array1, n);
}
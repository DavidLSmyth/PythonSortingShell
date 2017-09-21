#include <stdio.h>
#include <math.h>
#include <string.h>
#include "sorting_functions.h"

int main(){
	//the size of the array
	int n = 10;
	int array [10] = {9,6,4,3,2,11,16,20, 12, 15};
	int array1[10];
	int array2[10];
	memcpy(&array1, &array, n*sizeof(int));
	memcpy(&array2, &array, n*sizeof(int));

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
	c_insertion_sort(array,n);
	array[0]=1;
	array[9] = 100;
	printf("array1: \n");
	printArray(array1, n);
	c_bubble_sort(array1, n);
	printf("array1 sorted: \n");
	printArray(array1, n);

	printf("merged lists: \n");
	int mergedLists[20];
	memcpy(&mergedLists[0], &array, sizeof(int)*n);
	memcpy(&mergedLists[n], &array1, sizeof(int)*n);
	printf("Pre-merged list: \n");
	printArray(&mergedLists[5], 15-5);
	merge(mergedLists,5,10,15);
	printf("Post-merged list: \n");
	printArray(&mergedLists[5], 15-5);

	printf("-------------------------------------------------\n\npre merge sorted lists: \n");
	printArray(array2, n);
	c_merge_sort(array2, 0, 5,10);
	printf("Sorted Array: ");
	printArray(array2, n);

}
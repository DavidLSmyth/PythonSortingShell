#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int simple_function(int echo_int) {
    return echo_int;
}

void add_one_to_string(char *input) {
    int ii = 0;
    for (; ii < strlen(input); ii++) {
        input[ii]++;
    }
}

char * alloc_C_string(void) {
    char* phrase = strdup("I was written in C");
    printf("C just allocated %p(%ld):  %s\n",
           phrase, (long int)phrase, phrase);
    return phrase;
}

void free_C_string(char* ptr) {
    printf("About to free %p(%ld):  %s\n",
           ptr, (long int)ptr, ptr);
    free(ptr);
}

// C program for insertion sort
#include <stdio.h>
#include <math.h>
 
/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n)
{
   int i, key, j;
   for (i = 1; i < n; i++)
   {
       key = arr[i];
       j = i-1;
 
       /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
       while (j >= 0 && arr[j] > key)
       {
           arr[j+1] = arr[j];
           j = j-1;
       }
       arr[j+1] = key;
   }
}
 
// A utility function ot print an array of size n
void printArray(int arr[], int n)
{
   int i;
   for (i=0; i < n; i++)
       printf("%d ", arr[i]);
   printf("\n");
}
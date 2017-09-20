// C program for insertion sort
#include <stdio.h>
#include <math.h>
#include "sorting_functions.h"
 
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

void bubbleSort(int arr[], int no_elements){
  int counter1, counter2;
  for(counter1; counter1<no_elements;counter1++){
    for(counter2;counter2<counter1-1;counter2++){
      if(arr[counter2]<arr[counter2+1]){
        swap(& array[counter2], & array[counter2+1])
      }
    }
  }
}

//a utility function that swaps the position of i & j in an array
//takes in a pointer to i, a pointer to j and swaps the values based on the following logic: 
void swap(int *i, int *j){
  printf("i:%d j:%d \n", *i, *j);
  //temp takes on the value of i
  int temp = *i;
  printf("temp: %d\n", temp);
  //i points at j
  *i=*j;
  //j takes on the value of temp
  *j = temp;
}

 
// A utility function ot print an array of size n
void printArray(int arr[], int n)
{
   int i;
   for (i=0; i < n; i++)
       printf("%d ", arr[i]);
   printf("\n");
}
// C program for insertion sort
#include <stdio.h>
#include <math.h>
#include <string.h>
#include "sorting_functions.h"

/* Function to sort an array using insertion sort*/
__declspec(dllexport) void c_insertion_sort(int arr[], int n)
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

__declspec(dllexport) void c_bubble_sort(int arr[], int no_elements){

  for(int counter1=0; counter1 < no_elements; counter1++){
    for(int counter2 =0 ; counter2< no_elements-(counter1)-1; counter2++){
      if(arr[counter2]>arr[counter2+1]){
        swap(& arr[counter2], & arr[counter2+1]);
      }
    }
  }
}

__declspec(dllexport) void c_merge_sort(int arr[], int no_elements){
  c_merge_sort_implementation(arr, 0, no_elements/2, no_elements);
}

//c_merge_sort is really just a wrapper for c_merge_sort implementation
__declspec(dllexport) void c_merge_sort_implementation(int arr[], int ll_start, int midpoint, int rl_end){
  if(rl_end-ll_start>1){
    //c_merge_sort gets placed on the stack
    /*
    printf("ll_start: %d, midpoint: %d, rl_end: %d\n", ll_start, midpoint, rl_end);
    printf("ll: \t");
    printArray(&arr[ll_start], midpoint-ll_start);
    printf("rl: \t");
    printArray(&arr[midpoint], rl_end-midpoint);
    printf("\n");
    */
    //place on stack in this order
    c_merge_sort_implementation(arr, ll_start, (ll_start+midpoint)/2, midpoint);
    c_merge_sort_implementation(arr, midpoint, (midpoint+rl_end)/2, rl_end);
    merge(arr, ll_start, midpoint, rl_end);
    //printf("merged portion %d-%d\n", ll_start, rl_end);
  }
}


//a utility function that swaps the position of i & j in an array
//takes in a pointer to i, a pointer to j and swaps the values based on the following logic:
__declspec(dllexport) void swap(int *i, int *j){
  //
  //temp takes on the value of i
  int temp = *i;
  //
  //value of i equal to value of j
  *i=*j;
  //j takes on the value of temp
  *j = temp;
}

__declspec(dllexport) void merge(int array [], int ll_start, int midpoint, int rl_finish){
  //mergesort is most easily done by passing by reference in c. Rather than memcpying often, pass indices
  //and the arrays raw
  //merges subarrays array[start, midpoint] and array[midpoint, finish]. This is specific to mergesort

  int counter1 = 0;
  int counter2 = 0;

  int array1 [midpoint-ll_start];
  int array2 [rl_finish-midpoint];
  memcpy(&array2, &array[midpoint], sizeof(int) * (rl_finish-midpoint));
  memcpy(&array1, &array[ll_start], sizeof(int) * (midpoint-ll_start));
  //int array1_size = array1_finish-ll_start;
  //int array2_size = rl_finish-array2_start;
  int return_array_counter = ll_start;

  //printArray(array,(rl_finish - ll_start));
  //printArray(array1, midpoint-ll_start);
  //printArray(array2, rl_finish-midpoint);
  //int return_array_counter = 0;
  while((counter1<(midpoint-ll_start)) & (counter2<rl_finish-midpoint)){
    if(array1[counter1]<array2[counter2]){
      //printf("setting array[%d] = array[%d] -> array[%d] = %d\n", return_array_counter, counter1, return_array_counter, array1[counter1]);
      array[return_array_counter] = array1[counter1];
      counter1++;
    }
    else{
      //printf("setting array[%d] = array[%d] -> array[%d] = %d\n", return_array_counter, counter2, return_array_counter, array2[counter2]);

      array[return_array_counter] = array2[counter2];

      counter2++;
    }
    return_array_counter++;
    //printf("return counter: %d, counter1: %d, counter2: %d\n", return_array_counter, counter1, counter2);
    //printArray(array, 10);
    //printf("\n\n");
  }

  if(counter1 == (midpoint-ll_start)){
    //printf("Concatenating end of array2\n");
    //printArray(&array2[counter2], rl_finish-midpoint-counter2);
    while(counter2<rl_finish-midpoint){
      array[return_array_counter] = array2[counter2];
      //printArray(array,(rl_finish - ll_start));
      //printf("\n\n");
      counter2++;
      return_array_counter++;
    }
    //printArray(array,(10));
  }
  if(counter2 == (rl_finish-midpoint)){
    //printf("Concatenating end of array1\n");
    //printArray(&array1[counter1], midpoint-ll_start-counter1);
    while(counter1<midpoint-ll_start){
      array[return_array_counter] = array1[counter1];
      //printArray(array,(rl_finish - ll_start));
      //printf("\n\n");
      counter1++;
      return_array_counter++;
    }
    //printArray(array,(10));
  }
  //return return_array;
}


// A utility function ot print an array of size n
// A utility function ot print an array of size n
__declspec(dllexport) void printArray(int arr[], int n)
{
  int i;
  for (i=0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n");
}
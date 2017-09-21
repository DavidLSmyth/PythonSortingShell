// C program for insertion sort
#include <stdio.h>
#include <math.h>
#include <string.h>
#include "sorting_functions.h"
 
/* Function to sort an array using insertion sort*/
void c_insertion_sort(int arr[], int n)
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

void c_bubble_sort(int arr[], int no_elements){
  
  for(int counter1=0; counter1 < no_elements; counter1++){
    for(int counter2 =0 ; counter2< no_elements-(counter1)-1; counter2++){
      if(arr[counter2]>arr[counter2+1]){
        swap(& arr[counter2], & arr[counter2+1]);
      }
    }
  }
}
/*
void c_merge_sort(int arr[], int no_elements){
  if(no_elements>1){
    int left_arr [no_elements/2];
    int right_arr [no_elements-(no_elements/2)];
    //int return_array [no_elements];
    memcpy(&left_arr, &arr, no_elements/2);
    memcpy(&right_arr, &arr[no_elements/2],no_elements-(no_elements/2));
    merge(c_merge_sort(left_arr, no_elements/2), no_elements/2,c_merge_sort(right_arr, no_elements - (no_elements/2)),no_elements - (no_elements/2));
  }

}
*/

//a utility function that swaps the position of i & j in an array
//takes in a pointer to i, a pointer to j and swaps the values based on the following logic: 
void swap(int *i, int *j){
  //
  //temp takes on the value of i
  int temp = *i;
  //
  //value of i equal to value of j
  *i=*j;
  //j takes on the value of temp
  *j = temp;
}

void merge(int array [], int array1_start, int midpoint, int array2_finish){
  //mergesort is most easily done by passing by reference in c. Rather than memcpying often, pass indices
  //and the arrays raw
  //merges subarrays array[start, midpoint] and array[midpoint, finish]. This is specific to mergesort
  
  int counter1 = 0;
  int counter2 = 0;
  
  int array1 [midpoint-array1_start];
  int array2 [array2_finish-midpoint];
  memcpy(&array2, &array[midpoint], sizeof(int) * (array2_finish-midpoint));
  memcpy(&array1, &array[array1_start], sizeof(int) * (midpoint-array1_start));
  //int array1_size = array1_finish-array1_start;
  //int array2_size = array2_finish-array2_start;
  int return_array_counter = array1_start;
  
  printArray(array,(array2_finish - array1_start));
  printArray(array1, midpoint-array1_start);
  printArray(array2, array2_finish-midpoint);
  //int return_array_counter = 0;
  while((counter1<(midpoint-array1_start)) & (counter2<array2_finish-midpoint)){
    if(array1[counter1]<array2[counter2]){
      
      array[return_array_counter] = array1[counter1];
      counter1++;
    }
    else{
      

      array[return_array_counter] = array2[counter2];

      counter2++;
    }
    return_array_counter++;
    //
    printArray(array,(array2_finish - array1_start));
    
  }

  if(counter1 == (midpoint-array1_start)){
    
    while(counter2<array2_finish){
      array[return_array_counter] = array2[counter2];
      printArray(array,(array2_finish - array1_start));
      
      counter2++;
      return_array_counter++;
    }
  }
  if(counter2 == (array2_finish-midpoint)){
    
    while(counter1<midpoint){
      array[return_array_counter] = array1[counter1];
      printArray(array,(array2_finish - array1_start));
      
      counter1++;
      return_array_counter++;
    }
  }
  //return return_array;
}

 
// A utility function ot print an array of size n
void printArray(int arr[], int n)
{
   int i;
   for (i=0; i < n; i++)
       
   
}
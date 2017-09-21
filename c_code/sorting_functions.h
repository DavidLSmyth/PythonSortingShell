#ifndef sorting_functions_H_   /* Include guard */
#define sorting_functions_H_

void c_insertion_sort(int arr[], int n);
void c_bubble_sort(int arr[], int no_elements);
void swap(int *i, int *j);
void printArray(int arr[], int n);
//void merge(int array1 [], int array1_size,int array2 [], int array2_size, int return_array []);
void merge(int array [], int array1_start, int midpoint, int array2_finish);
void c_merge_sort(int arr[], int no_elements);
void c_merge_sort_implementation(int arr[], int ll_start, int midpoint, int rl_end);
#endif
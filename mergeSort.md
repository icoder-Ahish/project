# Merge Sort Implementation

This Markdown file presents a Python implementation of the **Merge Sort** algorithm.

---

## Explanation

Merge Sort is a **divide-and-conquer** sorting algorithm. It works by:
1.  **Dividing** the unsorted list into `n` sublists, each containing one element (a list of one element is considered sorted).
2.  **Conquering** by repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

## Python Code

```python
arr = [1,4,2,5,6,3,8]
st, end = 0, len(arr) - 1

def merge(arr, st, mid, end):
    """
    Merges two sorted subarrays of arr[st...mid] and arr[mid+1...end].
    """
    i, j = st, mid + 1
    temp = [] # Temporary list to store the merged elements

    # Compare elements from both subarrays and add the smaller one to temp
    while(i <= mid and j <= end):
        if(arr[i] <= arr[j]):
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            
    # Add remaining elements from the left subarray, if any
    while(i <= mid): # Corrected condition: should be 'mid' not '0'
        temp.append(arr[i])
        i += 1
            
    # Add remaining elements from the right subarray, if any
    while(j <= end): # Corrected condition: should be 'end' not '0'
        temp.append(arr[j])
        j += 1
            
    # Copy the sorted elements from temp back to the original array
    for k in range(len(temp)): # Renamed 'i' to 'k' for clarity in this loop
        arr[st + k] = temp[k]
        
def mergeSort(arr, st, end):
    """
    Recursively sorts the array arr using the Merge Sort algorithm.
    """
    if (st < end):
        mid = st + (end - st) // 2 # Calculate the middle index

        # Sort the left half
        mergeSort(arr, st, mid)
        # Sort the right half
        mergeSort(arr, mid + 1, end)
                
        # Merge the two sorted halves
        merge(arr, st, mid, end)
    
# Initial call to mergeSort
mergeSort(arr, st, end)

# Print the sorted array
print("Sorted array:")
for val in arr:
    print(val)

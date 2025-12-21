# Median of 2 sorted arrays 
def median(array1, array2):
    if len(array1) > len(array2):
        array1, array2 = array2, array1 # agar pehli array badi huwi toh swap karwaao
    
    m, n = len(array1), len(array2)
    min_bound, max_bound, half_len = 0, m, (m + n + 1) // 2
    
    # Binary search on the smaller array
    while min_bound <= max_bound:
        i = (min_bound + max_bound) // 2   # Partition index for array1
        j = half_len - i         # Partition index for array2
        
        # Adjust partition
        if i < m and array2[j-1] > array1[i]:
            min_bound = i + 1  # i is too small, move right
        elif i > 0 and array1[i-1] > array2[j]:
            max_bound = i - 1  # i is too big, move left
        else:
            # Found correct partition
            if i == 0:
                max_of_left = array2[j-1]
            elif j == 0:
                max_of_left = array1[i-1]
            else:
                max_of_left = max(array1[i-1], array2[j-1])
            
            #total length-odd matlab median is the greatest in left
            if (m + n) % 2 == 1:
                return max_of_left
            
            #Find min of right side
            if i == m:
                min_of_right = array2[j]
            elif j == n:
                min_of_right = array1[i]
            else:
                min_of_right = min(array1[i], array2[j])
            
            return (max_of_left + min_of_right) / 2.0


if __name__ == "__main__":
    arr1 = [1,3,9]
    arr2 = [2,6,9,20]
    print(median(arr1, arr2)) #1,2,3,6,9,9,20 ->>6

    arr3 = [1, 2]
    arr4 = [3, 4]
    print(median(arr3, arr4))  #1,2,3,4 ->>2.5
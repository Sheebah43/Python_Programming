# Median of 2 sorted arrays 
def median(array1, array2):
    merged = sorted(array1 + array2)
    n=len(merged)

    if n%2==1:
        return merged [n//2]
    else:
        return (merged[n//2-1] + merged[n//2])/2
if __name__ == "__main__":
    arr1 = [1,3,9]
    arr2 = [2,6,9,20]
    print(median(arr1, arr2)) #1,2,3,6,9,9,20 ->>6

    arr3 = [1, 2]
    arr4 = [3, 4]
    print(median(arr3, arr4))  #1,2,3,4 ->>2.5

# Rotate an array to the right by k-steps
def rotate_array(arr, steps):
    n = len(arr)
    if n == 0:
        return arr
    steps = steps % n #agar zaroorat se zyaada rotations karni padhi toh
    return arr[-steps:] + arr[:-steps]

array = [1, 2, 3, 4, 5, 6, 7]
k = int(input("Enter number of steps to rotate the array:\n"))
print("Demo array:", array)
print(f"Array after {k} steps rotation:", rotate_array(array, k))

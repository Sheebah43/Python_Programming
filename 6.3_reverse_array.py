# reverse an array with in place (.reverse)
def reverse(arr):
    arr.reverse()   
    return arr

if __name__ == "__main__":
    data1 = [1, 2, 3, 4, 5]
    print("Before reversing:", data1)
    print("After reversing:", reverse(data1[:]))  
    
    data2 = [20, 40, 60, 80, 100]
    print("Before reversing:", data2)
    print("After reversing:", reverse(data2[:]))

# Find the element that appears more than n/2 times 
def more_than_half_appearance(arr):
    n = len(arr)
    counts = {}

    for i in arr:
        counts[i] = counts.get(i, 0) + 1 # dictionary se no. of appearnces dekh rahe hain, agar nahi hoga toh +1 se pehla record aajaayega
        if counts[i] > n // 2:
            return i
    return -1

#length 6 hai, koi element 3 se zyaada dafa hona chahiye; nahi hai
print(more_than_half_appearance([37, 22, 21, 37, 46, 37])) 
#length 9 hai, koi element 4 se zyaada dafa hona chahiye; hai
print(more_than_half_appearance([784, 23, 784, 9, 11, 784, 2, 784, 784])) 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    
    # Partition
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # keep sorting left and right and eventually combine
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    data = [36, 2, 16, 9, 75, 8]
    print("Original:", data)
    print("Sorted:", quick_sort(data))

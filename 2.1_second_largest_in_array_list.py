#  WAP to find the second largest number
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements

    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

try:
    user_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, user_input.strip().split()))
    result = find_second_largest(nums)
    if result is not None:
        print("Second largest number is:", result)
    else:
        print("Not enough distinct numbers to determine second largest.")
except ValueError:
    print("Please enter valid integers only.")

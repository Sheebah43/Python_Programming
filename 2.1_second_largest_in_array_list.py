#  WAP to find the second largest number
def find_second_largest(numbers):
    nums = sorted(set(numbers))
    return nums[-2] if len(nums) >= 2 else None

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    forming_list = list(map(int, user_input.split()))
    found = find_second_largest(forming_list)

    if found is not None:
        print("Second largest number is:", found)
    else:
        print("Not enough distinct numbers to determine second largest.")

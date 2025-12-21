# Group words containing same letters together
# Input - an array / list as words
# Output - list of groups, where each group contains words with same letters { eat, tea... } G1, { tan, nat...} G2.

def group(words):
    groups = {}  # dictionary

    for word in words:
        # Sort letters in the word to form a key
        key = ''.join(sorted(word))
        
        # If key will not be present then initialize with empty list
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


if __name__ == "__main__": 
    words = ["eat", "tea", "tan", "cat", "nat", "rat"]
    result = group(words)

    print("Grouped words with same letters:")
    for i, group in enumerate(result, start=1):
        print(f"G{i}: {group}")



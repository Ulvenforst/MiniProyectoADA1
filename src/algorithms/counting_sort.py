def counting_sort(array, max_value, key=lambda x: x):
        counts = [0] * (max_value + 1)
        
        # Count the number of times each element appears in the array
        for item in array:
            counts[key(item)] += 1
        
        # Calculate the number of elements less than or equal to each element
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
        
        # Sort the array based on the counts
        sorted_array = [None] * len(array)
        for item in reversed(array):
            counts[key(item)] -= 1
            sorted_array[counts[key(item)]] = item
        
        return sorted_array

# Example usage
if __name__ == '__main__':
    array = [4, 2, 2, 8, 3, 3, 1]
    max_value = max(array)
    sorted_array = counting_sort(array, max_value)
    print(sorted_array)  # Output: [1, 2, 2, 3, 3, 4, 8]

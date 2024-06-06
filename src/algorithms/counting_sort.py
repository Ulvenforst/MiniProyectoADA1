# def counting_sort(array, max_value, key=lambda x: x):
#         counts = [0] * (max_value + 1)
        
#         # Count the number of times each element appears in the array
#         for item in array:
#             counts[key(item)] += 1
        
#         # Calculate the number of elements less than or equal to each element
#         for i in range(1, len(counts)):
#             counts[i] += counts[i - 1]
        
#         # Sort the array based on the counts
#         sorted_array = [None] * len(array)
#         for item in reversed(array):
#             counts[key(item)] -= 1
#             sorted_array[counts[key(item)]] = item
        
#         return sorted_array

def counting_sort(array, key=lambda x: x, reverse=False):
    max_value = max([key(value) for value in array])
    counts = [0] * (max_value + 1)

    # Count the number of times each element appears in the array
    for item in array:
        counts[key(item)] += 1

    if reverse:
        # Calculate the number of elements greater than or equal to each element
        for i in range(len(counts) - 2, -1, -1):
            counts[i] += counts[i + 1]
    else:
        # Calculate the number of elements less than or equal to each element
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

    # Sort the array based on the counts
    sorted_array = [None] * len(array)
    if reverse:
        for item in array:
            counts[key(item)] -= 1
            sorted_array[counts[key(item)]] = item
    else:
        for item in reversed(array):
            counts[key(item)] -= 1
            sorted_array[counts[key(item)]] = item

    return sorted_array

def bucket_sort(array, key=lambda x: x):
    if not array:
        return []

    # Determine the number of buckets
    num_buckets = len(array)
    buckets = [[] for _ in range(num_buckets)]

    # Determine min and max values to scale the bucket index
    min_value = min(key(item) for item in array)
    max_value = max(key(item) for item in array)
    range_value = max_value - min_value

    # Distribute the elements into buckets
    for item in array:
        normalized_value = (key(item) - min_value) / range_value
        bucket_index = min(num_buckets - 1, int(num_buckets * normalized_value))
        buckets[bucket_index].append(item)

    # Sort each bucket and concatenate the results
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket, key=key))

    return sorted_array


# def sort(array, key=lambda x: x):
#     if not array:
#         return []

#     if all(isinstance(key(item), int) for item in array):
#         max_value = max(key(item) for item in array)
#         return counting_sort(array, max_value, key)
#     elif all(isinstance(key(item), float) for item in array):
#         return bucket_sort(array, key)
#     else:
#         raise ValueError("Mixed data types or unsupported key type")

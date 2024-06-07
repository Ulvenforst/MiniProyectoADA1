def counting_sort(array, key=lambda x: x, reverse=False):
    max_value = max([key(value) for value in array])
    counts = [0] * (max_value + 1)

    for item in array:
        counts[key(item)] += 1

    if reverse:
        for i in range(len(counts) - 2, -1, -1):
            counts[i] += counts[i + 1]
    else:
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

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

def bucket_sort(array, key=lambda x: x, reverse=False):
    if not array:
        return array
    min_value = min(key(item) for item in array)
    max_value = max(key(item) for item in array)
    bucket_size = (max_value - min_value) // len(array) + 1
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]
    for item in array:
        normalized_key = key(item)
        index = (normalized_key - min_value) // bucket_size
        buckets[int(index)].append(item)
    index = 0
    if reverse:
        for bucket in reversed(buckets):
            insertion_sort(bucket, reverse=True)
            for item in bucket: 
                array[index] = item
                index += 1
    else:
        for bucket in buckets:
            insertion_sort(bucket, reverse=False)
            for item in bucket:
                array[index] = item
                index += 1
    return array

def insertion_sort(array, reverse=False):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and ((array[j] > key if not reverse else array[j] < key)):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


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

def bucket_sort(array, key=lambda x: x):
    if not array:
        return []

    num_buckets = len(array)
    buckets = [[] for _ in range(num_buckets)]

    min_value = min(key(item) for item in array)
    max_value = max(key(item) for item in array)
    range_value = 1 if max_value == min_value else max_value - min_value

    for item in array:
        normalized_value = (key(item) - min_value) / range_value
        bucket_index = min(num_buckets - 1, int(num_buckets * normalized_value))
        buckets[bucket_index].append(item)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket, key=key))

    return sorted_array

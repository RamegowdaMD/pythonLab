def array_operations(arr):
    def find_max_min(arr):
        return max(arr), min(arr)

    def find_second_largest(arr):
        unique_arr = list(set(arr))
        unique_arr.sort()
        return unique_arr[-2]

    max_value, min_value = find_max_min(arr)
    second_largest = find_second_largest(arr)

    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")
    print(f"Second largest value: {second_largest}")

array = [10, 20, 4, 45, 99, 99, 78]
array_operations(array)
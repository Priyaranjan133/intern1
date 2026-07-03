def second_largest(arr):
    if len(arr) < 2:
        return -1

    largest = second = -1

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


arr = [10, 20, 4, 45, 99]
print("Second Largest:", second_largest(arr))
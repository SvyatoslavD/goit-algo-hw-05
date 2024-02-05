def task2(arr, target):

    lim = None

    left, right = 0, len(arr) - 1

    iters = 0
    while left <= right:
        iters += 1
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            lim = arr[mid]
            right = mid - 1

    return (iters, lim)
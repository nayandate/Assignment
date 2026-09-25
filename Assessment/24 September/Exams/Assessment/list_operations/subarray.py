def minimum_subarray(numbers, target):
    start = 0
    total = 0
    minimum = len(numbers) + 1

    for end in range(len(numbers)):
        total = total + numbers[end]
        while total >= target:
            length = end - start + 1
            if length < minimum:
                minimum = length
            total = total - numbers[start]
            start = start + 1

    if minimum == len(numbers) + 1:
        return 0
    return minimum
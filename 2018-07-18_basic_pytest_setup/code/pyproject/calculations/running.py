def running_sum(numbers):
    """
    Lazily generate a running sum of an iterable of numbers.

    >>> list(running_sum([1, 2, 3]))
    [1, 3, 6]
    """
    current = 0

    for num in numbers:
        current += num

        yield current


def running_mean(numbers):
    """
    Lazily generate a running mean of an iterable of numbers.

    >>> list(running_mean([10, 20, 60]))
    [10.0, 15.0, 30.0]
    """
    for length, sum_so_far in enumerate(running_sum(numbers), start=1):
        mean = sum_so_far / length

        yield mean

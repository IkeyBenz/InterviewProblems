def sequence(start, end, fn=lambda i: i):
    """
        Returns list of numbers from start to end.
        If a function is supplied, the list of numbers will be mapped by that function.

        :param {int}  start The desired start value for the sequence
        :param {int}  end   The desired end value for the sequence
        :param {func} fn    Optional function that the numbers get mapped by
    """
    if start >= end:
        return []

    return list(fn(start)) + sequence(start + 1, end, fn)


def fizzbuzz(start, end):
    def fizzbuzz_of(num):
        if num % 3 == num % 5 == 0:
            return "FizzBuzz"
        if num % 3 == 0:
            return "Fizz"
        if num % 5 == 0:
            return "Buzz"
        return num
    return sequence(start, end, fizzbuzz_of)


if __name__ == '__main__':
    print(fizzbuzz(0, 12))
    # ['FizzBuzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11]

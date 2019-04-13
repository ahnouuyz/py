def letters_to_nums(letters):
    """ Convert letters to numbers.
        Use a-z as a base 26 system, with a = 1.
    """
    nums = list(map(lambda x: ord(x) - ord('a') + 1, letters.lower()))
    if all([num in range(1, 27) for num in nums]):
        return sum([v * (26 ** i) for i, v in enumerate(nums[::-1])])

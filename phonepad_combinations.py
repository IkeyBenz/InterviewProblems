letters = {
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' '
}

# Ikey's Way


def combos(nums, curr=[]):
    if len(nums) == 0:
        return curr
    if len(curr) == 0:
        return combos(nums[1:], list(letters[nums[0]]))

    extended = []
    for combo in combos:
        for letter in letters[nums[0]]:
            extended.append(combo + letter)

    return combos(nums[1:], extended)

# Alan's Way (cleaner cause no optional param)


def combos2(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return list(letters[nums])

    all_combos = []
    for combo in combos2(nums[1:]):
        for letter in letters[nums[0]]:
            all_combos.append(combo + letter)

    return all_combos


def possible_words(nums):
    words = (combos(word) for word in nums.split('0'))


def test_combos():
    assert combos('123') == [
        'adg', 'adh', 'adi',
        'aeg', 'aef'
    ]

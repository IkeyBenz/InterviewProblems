'''
    Write a function to determine if a function is smashable or not.

    What is a smashable word?
    A word that can be broken down into other words one letter at a time.
    
    Ex:  "PAINT" => "PINT" => "TIN" => "IN" => "I"
                                        "IN" "NI"
                                        "IT" "TI"
                                        "IA" "AI"
                                        "IP" "PI"

    "Paint" is smashable because each time we remove a letter from it, it is
    still a valid word.


|   1   |   2   |   3   |   4   |
|   1   |   2   |   3   |   4   |
|   1   |   2   |   3   |   4   |
|   1   |   2   |   3   |   4   |

|   2   |   1   |   4   |   3   |
|   2   |   1   |   1   |   4   | 
|   2   |   1   |   4   |   1   | 
|   2   |   1   |   3   |   3   |  

|   3   |   4   |   1   |   2   |
|   3   |   4   |   1   |   2   |
|   3   |   4   |   1   |   2   |
|   3   |   4   |   1   |   2   |

|   4   |   3   |   2   |   1   |
|   4   |   3   |   2   |   1   |
|   4   |   3   |   2   |   1   |
|   4   |   3   |   2   |   1   |


'''


def _is_word_valid(word: str) -> bool:
    valid_words = set(open('/usr/share/dict/words').read().splitlines())
    return lambda word: word in valid_words


is_word_valid = _is_word_valid()


def permutations(lst):
    for el in lst:


def is_smashable(word: str) -> bool:
    # Test and see if any characters solo are valid words, and work backwards
    ending_chars = set(map(list(word), is_word_valid))

    # Make combos of ending with remaining and get the valid ones
    for char in ending_chars:
        for other_char in set(word).difference(ending_chars):
            if

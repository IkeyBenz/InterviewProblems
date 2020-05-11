'''
You’re working an internship at Twitter and are tasked to improve suggestions for accounts to follow,
which already works great for established accounts because it uses content from your tweets and other
accounts you follow to suggest new ones. However, when a new user signs up none of this information
exists yet, but Twitter still wants to make some follow suggestions. Your team asked you to implement
a function that accepts a new user’s handle and an array of many other users’ handles, which could be
very long – Twitter has over 330 million active accounts! You need to calculate a similarity score
between a pair of handles by looking at the letters each contains, scoring +1 for each letter in the
alphabet that occurs in both handles but scoring –1 for each letter that occurs in only one handle.
Your function should return k handles from the array that have the highest similarity score to the new
user’s handle.
'''


def similarity_score(handle1: str, handle2: str) -> int:
    '''
        Given two strings, will output a number (the 'similarity score') between them
    '''
    handle1_set, handle2_set = set(handle1.lower()), set(handle2.lower())
    num_same = len(handle1_set.intersection(handle2_set))
    num_diff = len(handle1_set.symmetric_difference(handle2))

    return num_same - num_diff


def get_similar_handles_to(handle: str, handles: [str], k: int, compare=similarity_score) -> [str]:
    '''
        Given a string, a list of strings, and a number (k), will output the k most
        similar strings that are found in the provided list of handles.
        :param {function} compare? an optional parameter for a custom comparison (of two strings) function
    '''
    assert len(handles) > 0, "Handles cannot be empty"
    assert len(handles) > k, "K cannot be greater than the num of provided handles"

    scores_to_handles = {}
    for index, other_handle in enumerate(handles):
        score = compare(handle, other_handle)
        if score not in scores_to_handles:
            scores_to_handles[score] = []
        scores_to_handles[score].append(other_handle)

    ordered_scores = sorted(scores_to_handles.keys())
    ordered_handles = [**scores_to_handles[score] for score in ordered_scores]

    return ordered_handles[:k]

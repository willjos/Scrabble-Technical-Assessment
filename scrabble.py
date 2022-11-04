tile_dict = {'one_pt': ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
'two_pt': ['D', 'G'],
'three_pt': ['B', 'C', 'M', 'P'],
'four_pt': ['F', 'H', 'V', 'W', 'Y'],
'five_pt': ['K'],
'eight_pt': ['J', 'X'],
'ten_pt': ['Q', 'Z,']}


def score_for_word(word):
    score = 0
    for letter in word:
        if tile in
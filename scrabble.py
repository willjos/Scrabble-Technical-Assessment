tile_dict = {'one_pt': ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
'two_pt': ['D', 'G'],
'three_pt': ['B', 'C', 'M', 'P'],
'four_pt': ['F', 'H', 'V', 'W', 'Y'],
'five_pt': ['K'],
'eight_pt': ['J', 'X'],
'ten_pt': ['Q', 'Z,']}


def score_for_word(word):
    word_list = list(word.upper())
    score = 0
    for letter in word_list:
        if letter in tile_dict['one_pt']:
            score += 1
        elif letter in tile_dict['two_pt']:
            score += 2
        elif letter in tile_dict['three_pt']:
            score += 3
        elif letter in tile_dict['four_pt']:
            score += 4
        elif letter in tile_dict['five_pt']:
            score += 5
        elif letter in tile_dict['eight_pt']:
            score += 8
        elif letter in tile_dict['ten_pt']:
            score += 10
    return score


import random



tile_dict = {'one_pt': ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
'two_pt': ['D', 'G'],
'three_pt': ['B', 'C', 'M', 'P'],
'four_pt': ['F', 'H', 'V', 'W', 'Y'],
'five_pt': ['K'],
'eight_pt': ['J', 'X'],
'ten_pt': ['Q', 'Z,']}

tile_distribution = {'twelve_occ': ['E'],
'nine_occ': ['A', 'I'],
'eight_occ': ['O'],
'six_occ': ['N', 'R', 'T'],
'four_occ': ['L', 'S', 'U', 'D'],
'three_occ': ['G'],
'two_occ': ['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y'],
'one_tile': ['K', 'J', 'X', 'Q', 'Z']
}


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

def generate_bag():
    tile_bag = []
    for current_key in tile_distribution:
        if current_key == 'twelve_occ':
            for i in range(12):
                for tile in tile_distribution['twelve_occ']:
                    tile_bag.append(tile)
        if current_key == 'nine_occ':
            for i in range(9):
                for tile in tile_distribution['nine_occ']:
                    tile_bag.append(tile)
        if current_key == 'eight_occ':
            for i in range(8):
                for tile in tile_distribution['eight_occ']:
                    tile_bag.append(tile)
        if current_key == 'six_occ':
            for i in range(6):
                for tile in tile_distribution['six_occ']:
                    tile_bag.append(tile)
        if current_key == 'four_occ':
            for i in range(4):
                for tile in tile_distribution['four_occ']:
                    tile_bag.append(tile)
        if current_key == 'three_occ':
            for i in range(3):
                for tile in tile_distribution['three_occ']:
                    tile_bag.append(tile)
        if current_key == 'two_occ':
            for i in range(2):
                for tile in tile_distribution['two_occ']:
                    tile_bag.append(tile)
        if current_key == 'one_occ':
            for i in range(1):
                for tile in tile_distribution['one_occ']:
                    tile_bag.append(tile)
    return tile_bag

def shuffle_bag(bag):
    random.shuffle(bag)
    return bag

def generate_rack(shuffled_bag):
    rack = []
    for i in range(7):
        rack.append(shuffled_bag.pop())
    return rack

def check_valid_word(word):
    is_valid = 0
    with open('dictionary.txt', 'r') as f:
        for line in f:
            if line.strip('\n') == word:
                is_valid = 1
    return is_valid     

print(check_valid_word('hello'))
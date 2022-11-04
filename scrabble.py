import random

tile_dict = {'one_pt': ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'], # dict keys integers?
'two_pt': ['D', 'G'],
'three_pt': ['B', 'C', 'M', 'P'],
'four_pt': ['F', 'H', 'V', 'W', 'Y'],
'five_pt': ['K'],
'eight_pt': ['J', 'X'],
'ten_pt': ['Q', 'Z']}

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
    for letter in word_list: # if keys were integers, loop through tile dict for each tile dict, if letter in tile dict , score += key for tile dict
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

def generate_rack(shuffled_bag): # slice from 0 to 7 from shuffled bag
    rack = []
    for i in range(7):
        rack.append(shuffled_bag.pop())
    return rack

def check_valid_word(word):
    is_valid = 0
    with open('dictionary.txt', 'r') as f:
        for line in f:
            if line.strip('\n') == word: # send to Seb
                is_valid = 1
    return is_valid     

def find_words_in_rack(rack):
    words_in_rack = []
    with open('dictionary.txt', 'r') as f:
        for line in f:
            rack_copy = rack.copy()   # copy of the rack to work with 
            split_line = list(line.strip('\n').upper()) # list version of the current word to work with 
            is_in_rack = 0
            for letter in split_line:   # loop through each letter in the line
                if letter in rack_copy: # if the letter is in the rack copy, is in rack is true and we remove that letter from the rack copy
                    is_in_rack = 1
                    rack_copy.remove(letter) # this is where the magic happens...
                else:                   # if the letter is not in the rack copy, we know the word can't be made so we move on to the next line
                    is_in_rack = 0
                    break
            if(is_in_rack):
                words_in_rack.append(line.strip('\n').upper()) # consider converting dict to list and stripping all \n.     
    return words_in_rack
    
def find_longest_words_in_rack(rack):
    words_in_rack = find_words_in_rack(rack)
    max_length = len(max(words_in_rack, key=len))
    longest_words_in_rack = list(filter(lambda a: len(a) == max_length, words_in_rack))
    return {max_length: longest_words_in_rack}

def find_highest_score_in_rack(rack):
    words_in_rack = find_words_in_rack(rack)
    scores_in_rack = list(map(score_for_word, words_in_rack))
    max_score_in_rack = max(scores_in_rack)
    return max_score_in_rack

def find_max_score_words_in_rack(rack):
    words_in_rack = find_words_in_rack(rack)
    highest_scoring_words = [word for word in words_in_rack if(score_for_word(word) == find_highest_score_in_rack(rack))]
    return {score_for_word(highest_scoring_words[0]): highest_scoring_words}

def find_max_score_word_triple(rack): # this doesn't work, ZAX is better..
    words_in_rack = find_words_in_rack(rack)
    max_triple_score = 0
    best_word = ''
    for word in words_in_rack:
        for letter in list(word):
            score = (score_for_word(word[word.index(letter)]) * 2) + score_for_word(word)
            if score > max_triple_score:
                best_word = word
                max_triple_score = score
    return {best_word: max_triple_score}



# loop through words in rack
#       nest loop through each letter of the word
#           calculate points for word if that letter is a triple.
#           if points for the word > max_triple_score:
#                max_triple_score = points for the word


# test code:

test_rack = ['A', 'C', 'E', 'R', 'X', 'Y', 'Z']

print(find_words_in_rack(test_rack))     
print(find_longest_words_in_rack(test_rack))
print(find_highest_score_in_rack(test_rack))
print(find_max_score_words_in_rack(test_rack))
print(find_max_score_word_triple(test_rack))
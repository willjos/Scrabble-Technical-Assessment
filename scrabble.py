import random

tile_dict = {
    1:  ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'], # dict keys integers?
    2:  ['D', 'G'],
    3:  ['B', 'C', 'M', 'P'],
    4:  ['F', 'H', 'V', 'W', 'Y'],
    5:  ['K'],
    8:  ['J', 'X'],
    10: ['Q', 'Z']
}

tile_distribution = {
    12: ['E'],
    9:  ['A', 'I'],
    8:  ['O'],
    6:  ['N', 'R', 'T'],
    4:  ['L', 'S', 'U', 'D'],
    3:  ['G'],
    2:  ['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y'],
    1:  ['K', 'J', 'X', 'Q', 'Z']
}

def score_for_word(word):
    word_list = list(word.upper())
    score = 0
    for letter in word_list:
        for key in tile_dict:
            if letter in tile_dict[key]:
                score += key
    return score

def generate_bag():
    tile_bag = []
    for key in tile_distribution:
        for i in range(key):
            for tile in tile_distribution[key]:
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

def find_max_score_word_triple(rack):
    words_in_rack = find_words_in_rack(rack)
    max_triple_score = 0
    best_word = ''
    for word in words_in_rack:
        for letter in list(word):
            score = (score_for_word(word[word.index(letter)]) * 2) + score_for_word(word)
            if score > max_triple_score:
                best_word = word
                max_triple_score = score
    return {max_triple_score: best_word}

# test code:

test_rack = ['A', 'C', 'E', 'R', 'X', 'Y', 'Z']

print(find_words_in_rack(test_rack))     
print(find_longest_words_in_rack(test_rack))
print(find_highest_score_in_rack(test_rack))
print(find_max_score_words_in_rack(test_rack))
print(find_max_score_word_triple(test_rack))

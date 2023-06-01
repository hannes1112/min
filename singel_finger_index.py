import string
"""
Standard keyboard
y q w e r t z u i o p
y a s d f g h j k l
y y x c v b n m
0 x x x x x x x x x x

New keyboard
y a b c d e f g h i j
y k l m n o p k r s
y t u v w x y z
0 x x x x x x x x x x

The code compares the efficiency of the standard keyboard layout and a new keyboard
layout by calculating the Single-Finger Index for each word.
The Single-Finger Index measures how efficiently a word can be typed with
a single finger on the keyboard. The distance between letters is calculated,
considering slant distances and straight lines as one unit.
The lower the Single-Finger Index, the more efficient the word is to type.
The code aims to determine which keyboard layout is more efficient and its impact on typing speed.
"""

#index per letter pair
letter_positions = {
    'a': [2, 0, 0, 1],
    'b': [2, 1, 4, 0],
    'c': [2, 2, 2, 0],
    'd': [2, 3, 2, 1],
    'e': [2, 4, 2, 2],
    'f': [2, 5, 3, 1],
    'g': [2, 6, 4, 1],
    'h': [2, 7, 5, 1],
    'i': [2, 8, 7, 2],
    'j': [2, 9, 6, 1],
    'k': [1, 0, 7, 1],
    'l': [1, 1, 8, 1],
    'm': [1, 2, 6, 0],
    'n': [1, 3, 5, 0],
    'o': [1, 4, 8, 2],
    'p': [1, 5, 9, 2],
    'q': [1, 6, 0, 2],
    'r': [1, 7, 3, 2],
    's': [1, 8, 1, 1],
    't': [0, 0, 4, 2],
    'u': [0, 1, 6, 2],
    'v': [0, 2, 3, 0],
    'w': [0, 3, 1, 2],
    'x': [0, 4, 1, 0],
    'y': [0, 5, 0, 0],
    'z': [0, 6, 5, 2]
}

wordlist = ["Nuklearreaktorfachmitarbeiterkantine", "foobaa", "exampel"]

for current_word in wordlist:
    singel_finger_index_new = 0
    singel_finger_index_default = 0
    
    for current_word_letter in current_word.lower():
        if current_word_letter in letter_positions:
            letter_pos = letter_positions[current_word_letter]
            singel_finger_index_new += abs(letter_pos[0] - letter_pos[1])
            singel_finger_index_default += abs(letter_pos[2] - letter_pos[3])
        else:
            print("invalid char")
            exit()
            
    singel_finger_index_new /= len(current_word)
    singel_finger_index_default /= len(current_word)
    
    print(f"NEW: {singel_finger_index_new:.3f} OLD: {singel_finger_index_default:.3f} --> {current_word}")

"""
Standard keyboard
y q w e r t z u i o p
y a s d f g h j k l
y y x c v b n m
0 x x x x x x x x x x

New keyboard
a b c d e f g h i j
k l m n o p k r s
t u v w x y z

definition of a distance:
* A slant is a unit.
* A straight line is a unit.

All units in sum result in the index of a word. 
The less the index, the more efficient it is to type the word with one finger on the keyboard. 
"""

#index per letter pair
a_ = [2, 0, 0, 1]
b_ = [2, 1, 4, 0]
c_ = [2, 2, 2, 0]
d_ = [2, 3, 2, 1]
e_ = [2, 4, 2, 2]
f_ = [2, 5, 3, 1]
g_ = [2, 6, 4, 1]
h_ = [2, 7, 5, 1]
i_ = [2, 8, 7, 2]
j_ = [2, 9, 6, 1]
k_ = [1, 0, 7, 1]
l_ = [1, 1, 8, 1]
m_ = [1, 2, 6, 0]
n_ = [1, 3, 5, 0]
o_ = [1, 4, 8, 2]
p_ = [1, 5, 9, 2]
q_ = [1, 6, 0, 2]
r_ = [1, 7, 3, 2]
s_ = [1, 8, 1, 1]
t_ = [0, 0, 4, 2]
u_ = [0, 1, 6, 2]
v_ = [0, 2, 3, 0]
w_ = [0, 3, 1, 2]
x_ = [0, 4, 1, 0]
y_ = [0, 5, 0, 0]
z_ = [0, 6, 5, 2]

wordlist = ["Nuklearreaktorfachmitarbeiterkantine", "foobaa", "exampel"]

for current_word in wordlist:
    
    letter_pos = ""
    pos_x = []
    pos_y = []
    pos_x_deafult = []
    pos_y_deafult = []
    for current_word_letter in current_word:
        current_word_letter_lower = current_word_letter.lower()

        if current_word_letter_lower == "a":
            letter_pos = a_
        elif current_word_letter_lower == "b":
            letter_pos = b_
        elif current_word_letter_lower == "c":
            letter_pos = c_
        elif current_word_letter_lower == "d":
            letter_pos = d_
        elif current_word_letter_lower == "e":
            letter_pos = e_
        elif current_word_letter_lower == "f":
            letter_pos = f_
        elif current_word_letter_lower == "g":
            letter_pos = g_  
        elif current_word_letter_lower == "h":
            letter_pos = h_
        elif current_word_letter_lower == "i":
            letter_pos = i_
        elif current_word_letter_lower == "j":
            letter_pos = j_  
        elif current_word_letter_lower == "k":
            letter_pos = k_
        elif current_word_letter_lower == "l":
            letter_pos = l_
        elif current_word_letter_lower == "m":
            letter_pos = m_  
        elif current_word_letter_lower == "n":
            letter_pos = n_
        elif current_word_letter_lower == "o":
            letter_pos = o_
        elif current_word_letter_lower == "p":
            letter_pos = p_  
        elif current_word_letter_lower == "q":
            letter_pos = q_
        elif current_word_letter_lower == "r":
            letter_pos = r_
        elif current_word_letter_lower == "s":
            letter_pos = s_  
        elif current_word_letter_lower == "t":
            letter_pos = t_  
        elif current_word_letter_lower == "u":
            letter_pos = u_
        elif current_word_letter_lower == "v":
            letter_pos = v_
        elif current_word_letter_lower == "w":
            letter_pos = w_  
        elif current_word_letter_lower == "x":
            letter_pos = x_
        elif current_word_letter_lower == "y":
            letter_pos = y_
        elif current_word_letter_lower == "z":
            letter_pos = z_ 
        else:
            print("invalid char")
            exit()

        pos_x.insert(0, letter_pos[0])
        pos_y.insert(0, letter_pos[1])
        pos_x_deafult.insert(0, letter_pos[2])
        pos_y_deafult.insert(0, letter_pos[3])

    singel_finger_index_new = 0
    singel_finger_index_deafult = 0
    for i in range(len(current_word)):
        singel_finger_index_new     += abs(pos_x[i] - pos_y[i])
        singel_finger_index_deafult += abs(pos_x_deafult[i] - pos_y_deafult[i])

    singel_finger_index_new = singel_finger_index_new / len(current_word)
    singel_finger_index_deafult = singel_finger_index_deafult / len(current_word)
    
    print("NEW: {}--> {}".format(str(current_word), str(singel_finger_index_new)))
    print("OLD: {}--> {}".format(str(current_word), str(singel_finger_index_deafult)))

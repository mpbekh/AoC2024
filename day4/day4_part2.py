
char_matrix = []
count = 0

with open('input4.txt', "r") as input:
    # create matrix from input file
    lines = input.read().splitlines()
    for line in lines:
        char_matrix.append(list(line))

def is_xmas(chars):
    if ''.join(chars) == "MAS":
        return 1
    else:
        return 0

def read_dia_up_left(x, y):
    if x >= 2 and y >= 2:
        chars = [char_matrix[x-i][y-i] for i in range(3)]
        return is_xmas(chars)
    
def read_dia_up_right(x, y):
    if x >= 2 and y <= len(char_matrix[0])-3:
        chars = [char_matrix[x-i][y+i] for i in range(3)]
        return is_xmas(chars)
    
def read_dia_down_left(x, y):
    if x <= len(char_matrix)-3 and y >= 2:
        chars = [char_matrix[x+i][y-i] for i in range(3)]
        return is_xmas(chars)
    
def read_dia_down_right(x, y):
    if x <= len(char_matrix)-3 and y <= len(char_matrix[0])-3:
        chars = [char_matrix[x+i][y+i] for i in range(3)]
        return is_xmas(chars)

word_matrix = []
for x in range(len(char_matrix)):
    word_matrix.append([])
    for y in range(len(char_matrix[x])):
        # get words in all 4 diagonal directions outgoing from current x, y location
        mas_words = [
            read_dia_up_left(x, y),
            read_dia_up_right(x, y),
            read_dia_down_left(x, y),
            read_dia_down_right(x, y)
        ]
        word_matrix[x].append(mas_words)

# check for crossing partners
for x in range(len(word_matrix)):
    for y, diagonals in enumerate(word_matrix[x]):
        upleft, upright, downleft, downright = diagonals
        if upleft:
            # if upleft, check if crossing downleft or upright exist 
            if word_matrix[x-2][y][2] or word_matrix[x][y-2][1]:
                count += 1
        if downright:
            # if downright, check if crossing upright or downleft exist 
            if word_matrix[x+2][y][1] or word_matrix[x][y+2][2]:
                count += 1

print(count)

char_matrix = []
count = 0

with open('input4.txt', "r") as input:
    # create matrix from input file
    lines = input.read().splitlines()
    for line in lines:
        char_matrix.append(list(line))

def is_xmas(chars):
    if ''.join(chars) == "XMAS":
        return 1
    else:
        return 0

def read_right(x, y):
    # retrieve 4 chars right from index
    if y <= len(char_matrix[0])-4:
        chars = [char_matrix[x][y+i] for i in range(4)]
        return is_xmas(chars)

def read_left(x, y):
    # retrieve 4 chars left from index in reversed order
    if y >= 3:
        chars = [char_matrix[x][y-i] for i in range(4)]
        return is_xmas(chars)

def read_up(x, y):
    # retrieve upper 4 chars from index
    if x >= 3:
        chars = [char_matrix[x-i][y] for i in range(4)]
        return is_xmas(chars)

def read_down(x, y):
    # retrieve lower 4 chars from index
    if x <= len(char_matrix)-4:
        chars = [char_matrix[x+i][y] for i in range(4)]
        return is_xmas(chars)
    
def read_dia_up_left(x, y):
    if x >= 3 and y >= 3:
        chars = [char_matrix[x-i][y-i] for i in range(4)]
        return is_xmas(chars)
    
def read_dia_up_right(x, y):
    if x >= 3 and y <= len(char_matrix[0])-4:
        chars = [char_matrix[x-i][y+i] for i in range(4)]
        return is_xmas(chars)
    
def read_dia_down_left(x, y):
    if x <= len(char_matrix)-4 and y >= 3:
        chars = [char_matrix[x+i][y-i] for i in range(4)]
        return is_xmas(chars)
    
def read_dia_down_right(x, y):
    if x <= len(char_matrix)-4 and y <= len(char_matrix[0])-4:
        chars = [char_matrix[x+i][y+i] for i in range(4)]
        return is_xmas(chars)

for x in range(len(char_matrix)):
    for y in range(len(char_matrix[x])):
        # get words in all 8 directions outgoing from current x, y location
        xmas_words = [
            read_right(x, y),
            read_left(x, y),
            read_up(x, y),
            read_down(x, y),
            read_dia_up_left(x, y),
            read_dia_up_right(x, y),
            read_dia_down_left(x, y),
            read_dia_down_right(x, y)
        ]
        # add all occuring XMAS words from current location
        count += sum(filter(None, xmas_words))

print(count)
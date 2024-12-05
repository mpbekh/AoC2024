import re

# read columns from input and put into two lists
with open('input3.txt', "r") as input:
    text = input.read()

def multiply(x, y):
    return x*y

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.finditer(pattern, text)

sum = 0
for match in matches:
    sum += multiply(int(match.group(1)), int(match.group(2)))

print(sum)

# part 2

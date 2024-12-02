# part 1
list1=[]
list2=[]
 
# read columns from input and put into two lists
with open('input1.txt', "r") as input:
    lines = input.read().splitlines()
    for line in lines:
        split_line = line.split('   ')
        list1.append(int(split_line[0]))
        list2.append(int(split_line[1]))

# sort lists by size
list1 = sorted(list1)
list2 = sorted(list2)

# sum difference of lists
total_difference = 0
for i in range(len(list1)):
    total_difference += abs(list1[i] - list2[i])

print(f"Total difference (part 1): {total_difference}")


# part 2
sum_up = 0
for number in list1:
    sum_up += number * list2.count(number)

print(f"Sum up (part two): {sum_up}")

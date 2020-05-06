# https://www.codechef.com/problems/LUCKFOUR
# Problem Name: Lucky Four 
# Problem Code: LUCKFOUR
# Programming Lang: Python3
#
test = int(input())
ans_list = []
count =0
for x in range(test):
    
    new_in = int(input())
    new_in = int(new_in)
    while int(new_in) != 0:
        out = int(new_in) % 10
        new_in = int(new_in / 10)
        if out == 4:
            count = count + 1
    ans_list.insert(x, count)
    count = 0
x = 0
for x in range(len(ans_list)):
    print(ans_list[x])

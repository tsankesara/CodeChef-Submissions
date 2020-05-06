# https://www.codechef.com/problems/NUM239
# Problem Name: Counting Pretty Numbers
# Problem Code: NUM239
# Programming Lang: Python3

#ID => 32788017
#User => chefteerth (Me)

test = int(input())
if (1 <= test <=100):
    pass
else:
    exit()
ans_list = []
for x in range(test):
    counter = 0
    start, end = input().split(" ")
    start = int(start)
    end = int(end)
    if (start <= end and end <= 100000 and start >= 1):
        pass
    else:
        quit()
    while start != end+1:
        if start % 10 == 2:
            counter = counter+1
        if start % 10 == 3:
            counter = counter +1
        if start % 10 == 9:
            counter = counter +1
        start = start+1
    ans_list.insert(x, counter)
x = 0
for x in range(len(ans_list)):
    print(ans_list[x])

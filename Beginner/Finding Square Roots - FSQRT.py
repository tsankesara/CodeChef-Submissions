import math
test = int(input())
ans_lst = []

while 0 < test:
    k = int(input())
    k = int(math.sqrt(k)//1)
    ans_lst.append(k)
    test = test -1
for i in range(len(ans_lst)):
    print(ans_lst[i])
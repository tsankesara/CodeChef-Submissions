#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/JUNE20B/problems/XYSTR
# Problem Name: Chef and String
# Problem Code: XYSTR
# Programming Lang: Python3
test = int(input())
ans_lst = []

while 0 < test:
    string = input()
    i = 0
    temp = 0
    lenght = len(string)
    while i < lenght and i+1 < lenght:
        if string[i] != string[i+1]:
           temp = temp + 1
           i = i+2
           continue
        if string[i] == string[i+1]:
           i = i+1
           continue
    ans_lst.append(temp)
    test = test -1    
for x in range(len(ans_lst)):
    print(ans_lst[x])
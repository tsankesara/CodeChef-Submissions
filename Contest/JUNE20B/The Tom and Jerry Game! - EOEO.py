#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/JUNE20B/problems/EOEO
# Problem Name: The Tom and Jerry Game!
# Problem Code: EOEO
# Programming Lang: Python3

## Subtask Two is showing WA, so refer to C++ code of this for full solve
test = int(input())
ans_lsr = []

while 0 < test:
    TS = int(input())
    while TS % 2 == 0:
        TS = TS/2
    temp = int((TS-1)/2)
    ans_lsr.append(temp)
    test = test - 1 
for x in range(len(ans_lsr)):
    print(ans_lsr[x])       

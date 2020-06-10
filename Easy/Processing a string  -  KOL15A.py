#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/KOL15A
# Problem Name: Processing a string
# Problem Code: KOL15A
# Programming Lang: Python3

test = int(input())
i = 0
ans = []
while test > 0:
    temp = 0
    input_str = input()
    lenght = len(input_str)
    for x in range(lenght):
        if input_str[x] in "1234567890":
            num = int(input_str[x])
            temp = temp + num
    ans.append(temp)
    test = test -1
    
for x in range(len(ans)):
    print(ans[x])
            
## TRY if x in "123456789"

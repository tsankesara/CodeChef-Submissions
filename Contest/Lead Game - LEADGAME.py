#### THIS SOL IS WORKING BUT SHOWING WA ON CODE CHEF, GREAT IF ANYBODY COULD POIN OUT ISSUES###

#Username: chefteerth ## https://www.codechef.com/users/chefteerth
# Problem Name: Lead Game
# Problem Code: LEADGAME
# Programming Lang: Python3
p1_res = 0
p2_res = 0
test = int(input())
#if test > 10000:
#    quit() 
while test > 0:
    p1, p2 = input().split(" ")
    p1 = int(p1)
    p2 = int(p2)
 #   if p1 > 1000 or p2 > 1000:
  #      quit()
    if p1 > p2:
        if (p1-p2) >= p1_res:
            p1_res = (p1-p2)
    elif p2 > p1:
        if (p2-p1) >= p2_res:
            p2_res = (p2-p1)
    test = test - 1 
if p1_res > p2_res:
    print(1 ,p1_res)
else:
    print(2 ,p2_res)
    pass
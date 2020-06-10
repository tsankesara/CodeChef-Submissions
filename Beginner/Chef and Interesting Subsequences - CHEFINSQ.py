#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/CHEFINSQ
# Problem Name: Chef and Interesting Subsequences
# Problem Code: CHEFINSQ
# Programming Lang: Python3

from math import factorial as f
for i in range(int(input())):
    N,K=map(int,input().split())
    input_lst=list(map(int,input().split()))
    input_lst.sort()
    sumn=sum(input_lst[:K])
    p=input_lst[:K]
    a=p.count(p[-1])
    c=input_lst.count(p[-1])
    t=f(c)//(f(c-a)*f(a))
    print(t)
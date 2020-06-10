#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/PCO12020/problems/LOTR1
# Problem Name: Lord of the Rings
# Problem Code: LOTR1
# Programming Lang: Python3

# 1<= x <= M
# 1<= y <= N
test = int(input())
ans_lst = []
p =0
while p < test:
    x_lst = []
    no_of_pais = 0
    x=1
    y=1
    M, N = map(int,input().split())
    for x in range(1,M+1):
       for y in range(1,N+1):
            if (x*y) + (x+y) == int(str(x) + str(y)):
                no_of_pais = no_of_pais +1
                x_lst.append(x)
    ans = str(no_of_pais) + ' ' + str(len(x_lst))
    ans_lst.insert(p, ans)
    p = p + 1
for i in range(len(ans_lst)):
    print(ans_lst[i])
    
     
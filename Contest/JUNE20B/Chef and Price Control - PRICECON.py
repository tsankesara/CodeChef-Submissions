#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/JUNE20B/problems/PRICECON
# Problem Name: Chef and Price Control
# Problem Code: PRICECON
# Programming Lang: Python3

test = int(input())
ans_lst = []
while test > 0:
    after_lst = []
    N, K = map(int, input().split())
    curr_price = list(map(int,input().strip().split()))
    first_sum = sum(curr_price)
    i = 0
    for i in range(N):
        if curr_price[i] >  K:
            after_lst.append(K)
        else:
            after_lst.append(curr_price[i])
    loss =  first_sum - sum(after_lst)
    ans_lst.append(loss)
    test = test - 1
i = 0
for i in range(len(ans_lst)):
    print(ans_lst[i])
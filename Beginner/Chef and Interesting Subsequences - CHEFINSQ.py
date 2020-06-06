#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/CHEFINSQ
# Problem Name: Chef and Interesting Subsequences
# Problem Code: CHEFINSQ
# Programming Lang: Python3
test = int(input())
ans_lst = []
while 0 < test:
    sum_lst = []
    N, K = map(int, input().split(" "))
    lst_input = list(map(int, input().strip().split(" ")))
    node1 = 0
    while node1 < N:
        node2 = node1 + 1
        while node2 < N:
            if lst_input[node1] == K or lst_input[node2] == K:
                temp = lst_input[node1] + lst_input[node2]
                sum_lst.append(temp)
            node2 = node2 +1
        node1 = node1 + 1
    minm = min(sum_lst)
    ans = [k for k in range(len(sum_lst)) if sum_lst[k] == minm]
    ans_lst.append(len(ans))
    test = test - 1
for g in range(len(ans_lst)):
    print(ans_lst[g])
#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/JUNE20B/problems/CHFICRM
# Problem Name: Chef and Icecream
# Problem Code: CHFICRM
# Programming Lang: Python3

test = int(input())
ans_lst = []

while 0 < test:
    N = int(input())
    Money =  list(map(int,input().strip().split()))
    curr_money = []
    temp_ans = []
    for i in range(len(Money)):
        if Money[i] == 5:
            curr_money.append(5)
            continue
        if Money[i] == 10:
            Five_index_lst = [k for k in range(len(curr_money)) if curr_money[k] == 5]
            if len(Five_index_lst) == 0:
                temp_ans.append('NO')
                break
            else:
                curr_money.pop(Five_index_lst[0])
                curr_money.append(10)
        if Money[i] == 15:
            Five_index_lst = [k for k in range(len(curr_money)) if curr_money[k] == 5]
            Ten_index_lst = [k for k in range(len(curr_money)) if curr_money[k] == 10]
            if len(Five_index_lst) >= 1 and len(Ten_index_lst) >= 1:
                curr_money.append(15)
                curr_money.pop(Five_index_lst[0])
                curr_money.pop(Ten_index_lst[0])
            else: 
                temp_ans.append('NO')
                break

    if len(temp_ans) == 0:
        ans_lst.append('YES')
    else:
        ans_lst.append('NO')
    test = test -1
    
for x in range(len(ans_lst)):
    print(ans_lst[x])
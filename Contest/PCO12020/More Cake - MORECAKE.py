#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/PCO12020/problems/MORECAKE
# Problem Name: More Cake
# Problem Code: MORECAKE
# Programming Lang: Python3

test = int(input())
lst_sum = []
ans_list = []
p = 0
while p < test:
    i = 0
    llist = []
    TotalSlice, TotalMember, Smallest, R= map(int,input().split(" "))
    llist.append(Smallest)
    while TotalMember-1  > i:
        new_val = Smallest * R
        Smallest = new_val
        llist.append(new_val)
        i = i + 1
    if sum(llist) - TotalSlice <= 0:
        poss = "POSSIBLE" + str(TotalSlice - sum(llist))
        ans_list.insert(p, poss)
    else:
        poss = "IMPOSSIBLE" + str(abs(TotalSlice - sum(llist)))
        ans_list.insert(p, poss)
    lst_sum.append(sum(llist))
    p = p+1
for k in range(len(ans_list)):
    print(ans_list[k])
if sum(lst_sum) >= 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

    

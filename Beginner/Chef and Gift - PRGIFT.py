##Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/PRGIFT
# Problem Name: Chef and Gift
# Problem Code: PRGIFT
# Programming Lang: Python3
def gift(n,k):
    count = 0
    array = list(map(int,input().strip().split()))
    for i in array:
        if i % 2 == 0:
            count = count + 1
    if k==0 and count==n:
        return "NO"
    elif count<k:
        return "NO"
    else:
        return "YES"
test = int(input())
ans_lst = []
while 0 < test:
    n,k = map(int, input().split())
    ans = gift(n,k)
    ans_lst.append(ans)
    test = test -1
for x in range(len(ans_lst)):
    print(ans_lst[x])
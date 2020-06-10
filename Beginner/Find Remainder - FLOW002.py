def reminder(a,b):
    return a % b
test = int(input())
ans_lst = []
while 0 < test:
    a,b = map(int, input().split())
    ans = reminder(a,b)
    ans_lst.append(ans)
    test = test -1
for i in range(len(ans_lst)):
    print(ans_lst[i])
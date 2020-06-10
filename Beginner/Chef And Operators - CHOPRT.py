def Operator(a,b):
    if a > b:
        return ">"
    if a < b:
        return "<"
    if a == b:
        return "="
ans_lst = []
test = int(input())
while 0 < test:
    a,b = map(int, input().split())
    ans = Operator(a,b)
    ans_lst.append(ans)
    test = test -1
for i in range(len(ans_lst)):
    print(ans_lst[i])
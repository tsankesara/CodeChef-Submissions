def check(string):
    lst = []
    for i in range(len(string)):
        j = 1
        while j < len(string):
            pair = string[i] + string[j]
            lst.append(pair)
            if lst.count(pair) > 1:
                return "yes"
            j = j+1
    return "no"
test = int(input())
ans_lst = []

while 0 < test:
    ans = check(input())
    ans_lst.append(ans)
    test = test -1
for i in range(len(ans_lst)):
    print(ans_lst[i])
        
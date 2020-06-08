def Hosted(integ):
    year_ls = [2010,2015,2016,2017,2019]
    for i in range(len(year_ls)):
        if integ == year_ls[i]:
            return "HOSTED"
    return "NOT HOSTED"

test = int(input())
ans_lst = []
while 0 < test:
    ans = Hosted(int(input()))
    ans_lst.append(ans)
    test = test - 1
    
for i in range(len(ans_lst)):
    print(ans_lst[i])
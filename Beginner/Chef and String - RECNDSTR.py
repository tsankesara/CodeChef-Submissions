##Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/RECNDSTR
# Problem Name: Chef and String
# Problem Code: RECNDSTR
# Programming Lang: Python3
def LeftS(string):
    temp = string[0]
    newStr = slice(1,len(string))
    string = string[newStr] + temp
    return string
def RightS(string):
    temp = string[-1]
    newStr = slice(len(string)-1)
    string = temp + string[newStr]
    return string
test = int(input())
ans_lst = []
while 0 < test:
    string = input()
    if len(string) > 1:
        Lshift = LeftS(string)
        Rshift = RightS(string)
        if Lshift == Rshift:
            ans_lst.append("YES")
        else:
            ans_lst.append("NO")
    else:
        ans_lst.append("YES")       
    test = test -1

for i in range(len(ans_lst)):
    print(ans_lst[i])
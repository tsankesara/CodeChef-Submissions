def RightS(string):
    temp = string[-1]
    newStr = slice(len(string)-1)
    string = temp + string[newStr]
    return string
string = input()
Lshift = RightS(string)
print(Lshift)
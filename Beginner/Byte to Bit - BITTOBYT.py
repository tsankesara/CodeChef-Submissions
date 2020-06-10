##Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/BITOBYT
# Problem Name: Byte to Bit
# Problem Code: BITOBYT
# Programming Lang: Python3

def BytetoBit(Test):
    for i in range(Test):
        N = int(input())
        ans=0 
        k=0 
        bit,nibble,byte=0,0,0 
        N-=1 
        ans=int(N%26) 
        N/=26 
        k=int(pow(2,int(N)))
        if ans<2:
            bit=k 
        elif ans<10:
            nibble = k
        else:
            byte=k
        ans = str(bit) + ' ' + str(nibble) + ' ' + str(byte)
        return ans
test = int(input())
ans_lst = []
while 0 < test:
    ans = BytetoBit(test)
    ans_lst.append(ans)
    test = test -1
for i in range(len(ans_lst)):
    print(ans_lst[i])
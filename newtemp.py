# cook your dish here
T = int(input())
for i in range(T):
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
    
    print(bit,nibble,byte)
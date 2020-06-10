def Ans(N,H,duck,jump,L):
    count = 0
    i =1
    while i <= N: 
        T,X = map(int, input().split())
        if T == 1:
            if H-duck < X:
                count = count +1
                print('for Barrier: ' + str(i) + 'succefsfully ducked count: ' + str(count))
                i = i+1
                continue
            else:
                if L == 0:
                    print('L = 0: ' + str(count))
                    return "count recived from T =1 and L =0 "+ str(count)
                    
                else:
                    L =L-1
                    print('in Type = 1 '+'for Barrier: ' + str(i) + 'Life deplated count: ' + str(count))
                    i = i+1
                    count = count +1
                    continue
        else:
            if H+jump >= X:
                count = count +1
                print('for Barrier: ' + str(i) + 'succefsfully jumped count: ' + str(count))
                i = i+1
                continue
            else:
                if L == 0:
                    print('L = 0: ' + str(count))
                    return "count recived from T =2 and L =0 "+ str(count)
                else:
                    L= L-1
                    count = count +1
                    print('in type = 2' + 'for Barrier: ' + str(i) + 'Life deplated count: ' + str(count))
                    i = i+1
                    continue
    return "count recived from end"+ str(count)
            
            

test = int(input())
ans_lst = []
while 0 < test:
    N,H,Y1,Y2,L = map(int, input().split())
    ans_lst.append(Ans(N,H,Y1,Y2,L))
    test = test -1
for i in range(len(ans_lst)):
    print(ans_lst[i])
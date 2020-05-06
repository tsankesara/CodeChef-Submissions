# https://www.codechef.com/problems/MATCHES/
# Problem Name: Playing with Matches
# Problem Code: MATCHES
# Programming Lang: Python3

# ID => 32788586
# User => chefteerth (me)

def count(a):
    match = 0
    i = 0
    while len(a) > i:
        if a[i] == '0':
            match = match + 6
        if a[i] == '1':
            match = match + 2
        if a[i] == '2':
            match = match + 5
        if a[i] == '3':
            match = match + 5
        if a[i] == '4':
            match = match + 4
        if a[i] == '5':
            match = match + 5
        if a[i] == '6':
            match = match + 6
        if a[i] == '7':
            match = match + 3
        if a[i] == '8':
            match = match + 7
        if a[i] == '9':
            match = match + 6
        i = i+1   
    return match
        
test = int(input())
if (test<=1000 and 1 <= test):
    pass
else:
    exit()
j = 0
results_list = []
while test > j:
    num1, num2 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    if (1 <= num1 and num2 <= 1000000):
        pass
    else:
        exit()
    num3 = str(num1 + num2)
    results_list.insert(j, count(num3))
    j = j+1
for x in range(len(results_list)):
    print(results_list[x])

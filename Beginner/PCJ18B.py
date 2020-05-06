# https://www.codechef.com/problems/PCJ18B
# Problem Name: Chef and Bored Games
# Problem Code: PCJ18B
# Programming Lang: Python3



def square(n): 
  
    j = 0; 
  
    # For all odd values of i 
    for i in range(1, n + 1, 2): 
  
        # Add the count of possible 
        # squares of length i 
        k = n - i + 1; 
        j += (k * k); 
  
    # Return the required count
    j = int(j) 
    return j; 
  
test_cases = int(input())
test_list = []
counter = 0
while test_cases > counter:
    N = int(input())
    temp = square(N)
    test_list.insert(counter, temp)
    counter = counter + 1
for x in range(len(test_list)):
    print(test_list[x])

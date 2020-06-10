#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/TOTR
# Problem Name: The Tricky Deal
# Problem Code: TRICKYDL
# Programming Lang: Python3

test = int(input())
while test > 0:
    Total, Poss = map(int, input().split())
    start, lang = input().split(" ")
    if lang == 'H':
        alt_lang = 'E'
    else:
        alt_lang = 'H'
    if Total % 2 != 0:
        if lang == 'H':
            if Poss % 2 != 0:
                
                ans = lang
                
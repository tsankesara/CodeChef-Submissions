#Username: chefteerth ## https://www.codechef.com/users/chefteerth
#Question URL: https://www.codechef.com/problems/TOTR
# Problem Name: Tourist Translations
# Problem Code: TOTR
# Programming Lang: Python3
english = "abcdefghijklmnopqrstuvwxyz"
english = english + english.upper() + ".,!?"
lenght = 56
test, lang = input().split(" ")
lang = lang + lang.upper() + ".,!?"
test = int(test)
ans = []
while test  > 0:
    ans_str = ""
    sentence = input()
    sentence_len = len(sentence)
    for x in range(sentence_len):
        if sentence[x] == "_":
                ans_str = ans_str + " "
        else:
            inNo = english.index(sentence[x])
            ans_str = ans_str + lang[inNo]
    ans.append(ans_str)
    test = test -1
for i in range(len(ans)):
    print(ans[i])
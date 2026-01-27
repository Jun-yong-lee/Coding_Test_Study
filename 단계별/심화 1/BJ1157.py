import sys
input = sys.stdin.readline

words = list(input().rstrip().lower())
dict_word = {}
count = 0
max_key = ""

for each_word in words:
    dict_word[each_word] = dict_word.get(each_word, 0) + 1

max_value = max(dict_word.values())
for key in dict_word:
    if dict_word[key] == max_value:
        count += 1
        max_key = str(key)

if count != 1:
    print("?")
else:
    print(max_key.upper())
import sys
input = sys.stdin.readline

while True:
    res = []
    possible = True
    strings = str(input().rstrip())

    if strings[-1] != ".":
        print("no")
        continue
    if len(strings) == 1 and strings == ".":
        break

    strings_list = list(strings)
    for each_string in strings_list:
        if each_string in ["(", "["]:
            res.append(each_string)
        elif each_string in [")", "]"]:
            if len(res) == 0:
                possible = False
                break
            top = res[-1]

            if each_string == ")" and top == "(":
                res.pop()
            elif each_string == ")" and top != "(":
                possible = False
                break
                
            if each_string == "]" and top == "[":
                res.pop()
            elif each_string == "]" and top != "[":
                possible = False
                break
    if len(res) == 0 and possible == True:
        print("yes")
    else:
        print("no")

# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
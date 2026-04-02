def solution(phone_book):
    answer = True
    
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    
    for number in phone_book:
        prefix = ""
        for char in number:
            prefix += char
            if prefix in hash_map and prefix != number:
                answer = False
    return answer
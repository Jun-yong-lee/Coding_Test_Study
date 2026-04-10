def solution(numbers):
    s_numbers = list(map(str, numbers))
    
    s_numbers.sort(key=lambda x:x*4, reverse=True)
    
    return str(int("".join(s_numbers))) # "000" 예외처리 필수
def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for i, each_citation in enumerate(citations):
        if i + 1 > each_citation:
            return i
    return len(citations)
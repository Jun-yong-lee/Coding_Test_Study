def solution(sizes):
    n_sizes = []
    for i in range(len(sizes)):
        w, h = sizes[i]
        if w >= h:
            n_sizes.append([w, h])
        else:
            n_sizes.append([h, w])
    print(n_sizes)
    n_sizes.sort(key=lambda x:x[0], reverse=True)
    w_max = n_sizes[0][0]
    n_sizes.sort(key=lambda x:x[1], reverse=True)
    h_max = n_sizes[0][1]
    
    return w_max * h_max

def solution(sizes):
    width = [max(i) for i in sizes]
    height = [min(i) for i in sizes]
    
    return max(width) * max(height)
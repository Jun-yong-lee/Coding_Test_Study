def solution(rows, columns, queries):
    answer = []
    matrix = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        temp = matrix[x1][y1]
        min_val = temp

        # 왼쪽 세로줄
        for k in range(x1, x2):
            matrix[k][y1] = matrix[k+1][y1]
            min_val = min(min_val, matrix[k][y1])
        # 아래쪽 가로줄
        for k in range(y1, y2):
            matrix[x2][k] = matrix[x2][k+1]
            min_val = min(min_val, matrix[x2][k])
        # 오른쪽 세로줄
        for k in range(x2, x1, -1):
            matrix[k][y2] = matrix[k-1][y2]
            min_val = min(min_val, matrix[k][y2])
        # 위쪽 가로줄
        for k in range(y2, y1, -1):
            matrix[x1][k] = matrix[x1][k-1]
            min_val = min(min_val, matrix[x1][k])

        matrix[x1][y1+1] = temp
        answer.append(min_val)

    return answer
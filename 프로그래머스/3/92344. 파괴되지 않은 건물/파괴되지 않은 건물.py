def solution(board, skill):
    N = len(board)
    M = len(board[0])
    dp = [[0]*(M+2) for _ in range(N+2)]
    
    for tp,r1,c1,r2,c2,degree in skill:
        if tp==1: degree = -degree
        dp[r1+1][c1+1] += degree
        dp[r2+2][c2+2] += degree
        dp[r1+1][c2+2] -= degree
        dp[r2+2][c1+1] -= degree
        
    for i in range(1,N+1):
        for j in range(1,M+1):
            dp[i][j] = dp[i][j]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
            
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]+dp[i+1][j+1] > 0:
                answer += 1
    
    return answer
print('Welcome to Online IDE!! Happy Coding :)')
def answer(n):
    arr = [None]*(n+1)
    for i in range(n+1):
        arr[i] = [None]*(n+1)
        for j in range(n+1):
            arr[i][j] = 0
    
    arr[0][0] = 1
    for i in range(1, n+1):
        for j in range(n+1):
            arr[i][j] = arr[i-1][j]
            if j >= i:
                arr[i][j] += arr[i-1][j-i]
    return arr[n][n] - 1

if __name__ == '__main__':
    # This prints out the results of this function on any value between (including) 3 and 200.
    # It's just for debugging.
    print("Format:\n Number of Bricks --> Distinct Partitions")
    for bricks in range(3, 15):
        print('   ', bricks, " --> ", str(answer(bricks)))
        
#        print(solution(3))
#        print(solution(n2))

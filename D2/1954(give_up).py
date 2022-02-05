T = int(input())

for i in range(1,T+1):
    N = int(input())
    solve = []
    for j in range(N):
        a=[]
        for k in range(N):
            a.append(0)
        solve.append(a)
    

    # for a in range(N):
    #     for b in range(N):
    #         if a == 0 :
    #             solve[a][b] = b+1
    #         elif a == N-1 :
    #             solve[a][b] = 3*N -2 - b

    #         elif a <= b  and b < N-a:
    #             solve[a][b] = solve[a-1][a-1] + 4*N - 2*(a+1)**2 + 2*(a+1) + b-a
    
    cnt = 1
    num = 0
    for j in range(N):
        for a in range(N):
            if num % 4 == 0:
                solve[num][a] = cnt
                cnt +=1
                
            
            elif num % 4 == 1:
                solve[a][N-num-1] = cnt
                cnt +=1
                
                
            elif num % 4 == 2:
                solve[N-num][N-a-1] =cnt
                cnt +=1
                
            else :
                solve[N-a-1][num] =cnt
                cnt += 1
               
        num +=1



                

print(solve)
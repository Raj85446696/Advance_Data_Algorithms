def StrassenMatrix(A,B):
    C = [[0,0] for i in range(2)]
    a,b,c,d = A[0][0],A[0][1],A[1][0],A[1][1]
    e,f,g,h = B[0][0],B[0][1],B[1][0],B[1][1]

    # Calculate Strassen’s 7 multiplicationsStrassen’s 7 multiplications
    M1 = (a+d)*(e+h)
    M2 = (c+d)*e
    M3 = (a)*(f-h)
    M4 = d*(g-e)
    M5 = (a+b)*h
    M6 = (c-a)*(e+f)
    M7 = (b-d)*(g+h)

    # Final Matrix C 
    C[0][0] = M1+M4-M5+M7
    C[0][1] = M3+M5
    C[1][0] = M2+M4
    C[1][1] = M1-M2+M3+M6
    
    return C

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(StrassenMatrix(A,B))


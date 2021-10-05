def getLCS(X, Y): # X and Y should be the string.
    length1 = len(X)
    length2 = len(Y)
    LCS = [[0] * (length2+1) for _ in range(length1+1)]
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if X[i-1] == Y[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    return LCS
    #return LCS[length1][length2], length1, length2
        

def findLCS(LCS, X, len1, len2):
    result = []
    def recall(i, j): # i, j should be the LCS' index.
        if LCS[i][j] == 0:
            return result
        if LCS[i][j] == LCS[i-1][j]:
            recall(i-1, j)      
        elif LCS[i][j] == LCS[i][j-1]:
            recall(i, j-1)
        elif LCS[i][j] != LCS[i-1][j] and LCS[i][j] != LCS[i][j-1]:
            result.append(X[i-1])
            recall(i-1, j-1)
    recall(len1, len2)
    result.reverse()
    return result
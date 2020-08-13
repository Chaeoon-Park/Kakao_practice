#2진수 변환 함수  bin

def solution(n, arr1, arr2):
    answer = ['' for row in range(n)]
    for i in range(0,n) :
        v1 = bin(arr1[i])
        v1 = v1[2:]
        v2 = bin(arr2[i])
        v2 = v2[2:]

        if len(v1)<n :
            for j in range(0,n-len(v1)) :
                v1 = '0' + v1

        if len(v2)<n :
            for j in range(0,n-len(v2)) :
                v2 = '0' + v2
        for j in range(0,n) :
            if v1[j]==v2[j] and v1[j]=='0' :
                answer[i]= answer[i]+" "
            else :
                answer[i]= answer[i]+"#"
    return answer

solution(	5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
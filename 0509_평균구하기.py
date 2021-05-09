arr=[1,2,3,4]

def solution(arr):
    a=0
    for i in arr[0:]:
        a=a+i
        k=a/len(arr)
    return k
print (solution(arr))
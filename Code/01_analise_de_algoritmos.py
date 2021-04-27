#Recebe um arranjo A  e retorna o máximo valor
def max_array(A):
    max = A[0]
    i = 1
    
    while i < len(A):
        if A[i] > max:
            max = A[i]  
        i += 1

    return max

def max_min_array(A):
    max = min = A[0]
    i = 1
    
    while i < len(A):
        if A[i] > max:
            max = A[i]
        elif A[i] < min:
            min = A[i]
        i += 1

    return [max, min]


def linear_search(A, target):
    n = len(A)

    for i in range(n):
        if A[i] == target:
            return i
    
    return -1

if __name__ == "__main__":
    A = [6,2,3,4,5,6]
    print(linear_search(A, 6))
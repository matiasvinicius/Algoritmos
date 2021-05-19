def insertion_sort(A):
    end = len(A)
    i = 0
    j = 0

    while i < end:
        value = A[i]
        j = i
        while j>0 and A[j-1] > value:
            A[j] = A[j-1]
            j = j-1
        A[j] = value
        i += 1
    
    return A

def insertion_sort_rec(A, n):
    if n == 1: return 

    insertion_sort_rec(A, n-1)
    i = n - 1
    aux = 0

    while i > 0 and A[i-1] > A[i]:
        aux = A[i]
        A[i] = A[i-1]
        A[i-1] = aux
        i -= 1

    return A

def selection_sort(A):
    n = len(A)
    fim = n-1

    while fim > 0:
        max = fim
        for j in range(fim):
            if A[j] > A[max]:
                max = j
        if fim != max:
            temp = A[fim]
            A[fim] = A[max]
            A[max] = temp
        fim -= 1

    return A

def selection_sort_rec(A, n):
    if n == 1: return A
    
    max = n-1
    for i in range(n):
        if A[i] > A[max]:
            max = i
    
    if max != n-1:
        temp = A[max]
        A[max] = A[n-1]
        A[n-1] = temp

    return selection_sort_rec(A, n-1)

def bubble_sort(A, n):
    i = n-1
    
    while i > 0:
        j = 1
        while j <= i:
            if A[j-1] > A[j]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
            j += 1
        i -= 1
    
    return A

def bubble_sort_rec(A, n):
    i = 1
    while i < n:
        if A[i] < A[i-1]:
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
        i += 1
    return bubble_sort(A, n-1)

if __name__ == "__main__":
    A = [4,4,52,-6,2,20]

    print(bubble_sort_rec(A, len(A)))
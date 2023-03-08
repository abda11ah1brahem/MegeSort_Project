def mergeSort(A):
    #global lefthalf, righthalf, mid, mergrSort
    if len(A)> 1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]>righthalf[j]:
                A[k]=lefthalf[i]
                i+=1
            else:
                A[k]=righthalf[j]
                j+=1
            k+=1
        while i < len(lefthalf):
            A[k]=lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            A[k]=righthalf[j]
            j+=1
            k+=1
    return A
a=[5,6,1,3,2,4]
print(mergeSort(a))
#print(a)
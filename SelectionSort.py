def SelectionSort(arr):
    l=len(arr)
    for i in range(l-1):
        m=i
        for j in range(i+1,l):
            if arr[j]<arr[m]:
                m=j
        temp=arr[i]
        arr[i]=arr[m]
        arr[m]=temp
            

arr=list(map(int,input("Enter array: ").split()))
SelectionSort(arr)
print("Sorted Array:",*arr)

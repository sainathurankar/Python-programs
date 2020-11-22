def InsertionSort(arr):
    l=len(arr)
    for i in range(1,l):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=list(map(int,input("Enter array: ").split()))
InsertionSort(arr)
print("Sorted Array:",*arr)

def Partition(arr,s,e):
    pivot=arr[e]
    pIndex=s
    for i in range(s,e):
        if arr[i]<pivot:
            temp=arr[i]
            arr[i]=arr[pIndex]
            arr[pIndex]=temp
            pIndex+=1
    temp=arr[pIndex]
    arr[pIndex]=arr[e]
    arr[e]=temp
    return pIndex



def QuickSort(arr,s,e):
    if s<e:
        p=Partition(arr,s,e)
        QuickSort(arr,s,p-1)
        QuickSort(arr,p+1,e)
    
        

arr=list(map(int,input("Enter array elements: ").split()))
QuickSort(arr,0,len(arr)-1)
print("Sorted Array:",*arr)
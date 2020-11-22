def BubbleSort(arr):
    l=len(arr)
    for i in range(l):
        flag=0
        for j in range(l-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                flag=1
        if flag==0:break
            

arr=list(map(int,input("Enter array: ").split()))
BubbleSort(arr)
print("Sorted Array:",*arr)

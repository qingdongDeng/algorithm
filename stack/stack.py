def adjast(arr,s,e):
    tmp = s
    l = s * 2 +1
    r =  l + 1
    if s <= e/2 :
        if l <= e and int(arr[l]) < int(arr[tmp]):
            tmp = l
        if r <= e and int(arr[r]) < int(arr[tmp]):
            tmp = r
        if tmp != s :
            arr[s],arr[tmp] = arr[tmp],arr[s]
            adjast(arr,tmp,e)

def heapsort(arr,i,lenght):
    #从第一个非叶子节点，从右到左调整堆
    for j in range(int(i),-1,-1):
        adjast(arr,j,lenght)
    for j in range(int(lenght), -1 , -1):
        arr[0],arr[j] = arr[j],arr[0]
        if j > 0 :
            adjast(arr,0,j-1)

def main():
    n = input("请输入要排的n个数:\n")
    arr = input().strip().split()
    le = len(arr)
    print(arr)
    heapsort(arr,(le)/2 -1 , le-1 )
    print(arr)

if __name__ == '__main__':
    main()
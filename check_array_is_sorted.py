

if __name__  == "__main__":
    n: int = int(input("enter the values count: "))
    if n<=1:
        print("please ente rthe 2 values: ")
    else:
        arr: list[int] = list(map(int, input("enter the values: ").strip().split()))[:n]
        is_sorted: bool = all(arr[i] <= arr[i-1] for i in range(1, len(arr)))
        if is_sorted:
            print("The array is sorted in non-decreasing order.")
        else:
            print("The array is not sorted in non-decreasing order.")


def largest_element(arr: list[int]) -> int:
    largest: int = arr[0]
    for num in arr[1:]:  # start from second element
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    n = int(input("Enter the number of values: "))
    if n <= 0:
        print("Please enter at least one value.")
    else:
        arr = list(map(int, input("Enter the values: ").strip().split()))[:n]
        largest = largest_element(arr)
        print(f"The largest element in the series is {largest}")
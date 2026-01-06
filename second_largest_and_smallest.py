def second_largest(arr:list[int]) -> int:
    first: int = float('-inf')
    second: int = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

if __name__ == "__main__":
    n:int =int(input("enter the number of the values: "))
    if n <= 1:
        print("Please enter at least two values.")
    else:
        arr: list[int] = list(map(int, input(
            "Enter the values: ").strip().split()))[:n]
    second_largest:int = second_largest(arr)
    if second_largest == float('-inf'):
        print("There is no second largest element.")
    else:
        print(f"The second largest element in the series is {second_largest}")
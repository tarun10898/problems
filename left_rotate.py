class Solution:
    def __init__(self):
        pass

    def rotatearray(self, arr: list[int]) -> list[int]:
        first_element: int = arr[0]
        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]
        arr[-1] = first_element
        return arr

if __name__ == "__main__":
    n: int = int(input("Enter the values count: "))
    if n <= 0:
        print("Please enter valid values")
    else:
        arr: list[int] = list(map(int, input("Enter the values: ").strip().split()))[:n]
        sol = Solution()
        k: list[int] = sol.rotatearray(arr)
        print(f"The array after left rotation is: {k}")
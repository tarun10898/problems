
def leftrotate(arr:list[int],k:int) -> list[int]:
    n:int = len(arr)
    k = k % n
    rotated_arr:list[int] = arr[k:] + arr[:k]
    return rotated_arr

def rightrotate(arr:list[int],k:int) -> list[int]:
    n:int = len(arr)
    k %= n
    rotate_arr:list[int] = arr[-k:] + arr[: -k]
    return rotate_arr



if __name__ == "__main__":
    n:int = int(input("enter the number of values in the array: "))
    if n<0:
        print("please enter the valid values")
    else:
        arr:list[int] = list(map(int,input("enter the values of the array: ").strip().split()))[:n]
        k:int = int(input("enter the number of rotations: "))
        print(f"the array after left and right rotations are: {leftrotate(arr,k),rightrotate(arr,k)}")
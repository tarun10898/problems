



# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements: "))
#     count:int = 1 
#     if n <= 0:
#         print("please enter at least one element.")
#     else:
#         arr:list[int] = list(map(int,input("enter the elements :").strip().split()))[:n]
#         uniques_elements:set[int]= set()
#         for num in arr:
#             if num not in uniques_elements:
#                 uniques_elements.add(num)
#                 arr[count -1] = num
#                 count += 1
#     print(f"the array after removing duplicates is{count} :{arr[:count -1]}")            




# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements: "))
#     count:int = 1 
#     if n <= 0:
#         print("please enter at least one element.")
#     else:
#         arr:list[int] = list(map(int,input("enter the elements :").strip().split()))[:n]
#         uniques_elements:set[int]= set()
#         for num in arr:
#             if num not in uniques_elements:
#                 uniques_elements.add(num)
#                 arr[count -1] = num
#                 count += 1
#     print(f"the array after removing duplicates is{count} :{arr[:count -1]}")            
            
class Solution():
    def __init__(self):
        pass
    def removeDuplicates(self,arr:list[int]) -> int:
        i =0
        for j in range(1,len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]
        return i + 1

if __name__ == "__main__":
    n:int = int(input("enter the number of values:"))
    if n<0:
        print("please enter at least one value: ")
    else:
        arr:list[int] = list(map(int,input("enter the values: ")))[:n]
        sol = Solution()
        k:int =sol.removeDuplicates(arr)
        print(f"the array after removing duplicates is {k} :{arr[:k]}") 
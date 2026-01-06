def print_1_to_n(n:int) -> None:
    if n <= 0:
        return
    else:
        print_1_to_n(n - 1)
        print(n)


if __name__ == "__main__":
    n:int = int(input("enter the number:" ))
    if n<=0:
        print("please enter the valide number graer than 0")
    else:
        print_1_to_n(n)
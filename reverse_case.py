def swap_case(string):
    return string.swapcase()


if __name__ == "__main__":
    my_string = input("A phrase to have its case reversed:\n")
    print(swap_case(my_string))

def ascending(num: str) -> bool:
    # Start with a single digit
    digits = 1

    # Once we have a number of digits that mathematically rules out the next number being there, stop
    while digits <= len(num) / 2:
        # The current number
        current = int(num[:digits])

        # The number of digits of the next consecutive number determines the size of the bucket to retrieve
        next_size = len(str(current+1))

        # The starting index to look for the next consecutive number
        index = digits

        # Keep looking for ascending numbers until you would have an index out of bounds exception
        while next_size + index <= len(num):

            # The value of the number in the next bucket
            next_num = num[index:index+next_size]

            # If the numbers are not consecutive, then this loop won't find the answer
            if not consecutive(current, next_num):
                break

            index += next_size
            current = int(next_num)
            next_size = len(str(current+1))

        # Up the digit count
        digits += 1

        # If the loop concluded successfully, then return that the conditions are met
        if index == len(num):
            return True
    return False


def consecutive(num_1, num_2):
    return int(num_1) - int(num_2) in [1, -1]


if __name__ == "__main__":
    my_num = input("Input a number for testing:\n")
    print(ascending(my_num))

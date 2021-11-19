def square_patch(square_size):
    square = []
    for _ in range(square_size):
        row = []
        for _ in range(square_size):
            row.append(square_size)
        square.append(row)

    for row in square:
        print(row)


if __name__ == "__main__":
    size = int(input("What size square would you like?\n"))
    square_patch(size)

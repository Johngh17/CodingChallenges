def repeated(to_check):
    chars = 1
    substring = to_check[:chars]
    string_len = len(to_check)

    if string_len == 1:
        return True

    # Keep going until you get a string too long to repeat
    while len(substring) <= string_len / 2:
        # Check whether it is mathematically impossible first
        if string_len % len(substring) != 0:
            chars += 1
            substring = to_check[:chars]
            continue

        # This needs to be reset for every new potential repeating segment
        repeating = True

        # We need to check all of the segments
        # We can cast to int because we know that the modulus is 1
        for segmentNumber in range(int(string_len/len(substring))):
            repeating &= substring in to_check[segmentNumber * len(substring):(segmentNumber + 1) * len(substring)]

        # If any substring works, then we have our answer and don't even need to break the loop
        if repeating:
            return repeating

        # Clerical work to make the loop run properly
        chars += 1
        substring = to_check[:chars]

    return False


if __name__ == '__main__':
    your_word = input("String to check for repetition: \n")
    print(f"{your_word} does {(not repeated(your_word)) * 'not '}repeat")

def get_vowel_substrings(base):
    # For checking whether something is a vowel
    vowels = "AEIOUaeiou"

    # To hold results while avoiding duplicates
    substrings = set()

    # We need to iterate over the entire string but also need the indices to speed things up
    for i, char in enumerate(base):
        # Only do something special if we encounter a vowel
        if char in vowels:
            # The problem wants single letters, too, so we'll handle that here
            substrings.add(char)

            # Check the rest of the string
            for j, subChar in enumerate(base[i+1:]):
                # Any vowel encountered represents the end of a potentially unique substring
                if subChar in vowels:
                    # Add the substring to the results set
                    substrings.add(base[i:i+2+j])

    return sorted(list(substrings))


if __name__ == "__main__":
    string = input("Word or phrase to decompose: \n")
    print(get_vowel_substrings(string))

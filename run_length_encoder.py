# Run-Length Encoder/Decoder          10-20-25

# Goal
# Write two functions:

# encode(s: str) -> str
# Compresses a string by replacing consecutive runs of the same character with <count><char>

# decode(s: str) -> str
# Expands that compressed form back to the original string

# Rules
# A "run" is one or more identical characters in a row
# Always include the count, even if it's 1 (so "A" -> "1A")
# Treat every character literally - letters, spaces, digits, punctuation, all count
# Your decode() must handle multi-digit counts (like "12A" = 12 A's)
# Empty strings should round-trip cleanly:
# encode("") == ""
# decode("") == ""

# Examples

# Encoding
# Inputs             Output
# "AAABCCDDDD"       "3A1B2C4D"
# "HELLO"            "1H1E2L1O"
# "WWW!!!  "         "3W3!2 "
# "111223"           "3122231"
# ""                 ""

#Decoding
# Inputs             Output
# "3A1B2C4D"         "AAABCCDDDD"
# "1H1E2L1O"         "HELLO"
# "3W3!2 "           "WWW!!!  "
# "3122231"          "111223"
# ""                 ""

def encode(s: str) -> str:
    result = ""
    count = 1
    for i in range(len(s)):
        pass
    return result

def decode(s: str) -> str:
    pass

def main():
    s = str(input("What is your phrase?: "))
    print(encode(s))
    print(decode(encode(s))) 


if __name__ == "__main__":
    main()
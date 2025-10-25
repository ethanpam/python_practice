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
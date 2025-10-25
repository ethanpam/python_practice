def busesNeeded(total_people):
    count = 0
    while total_people > 50:
        total_people = total_people - 50
        count += 1
    return count + 1

def main():
    total_people = int(input("What is the total people riding the bus?: "))
    print(busesNeeded(total_people))

if __name__ == "__main__":
    main()
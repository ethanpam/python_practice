# COM S 1270 Exam #1 Practice Verison        10-20-25
# B) Buses Needed

# Each bus can carry 50 passengers. Write a function busesNeeded that
# Takes one parameter, total_people. You may assume that total_people will always be a positive integer greater than zero
# Returns how many buses are needed so everyone gets a seat

# Examples:
# busesNeeded(30) returns 1, because a bus holds 50 people, and 30 < 50
# busesNeeded(60) returns 2, because buses hold 50 people each, and a partial busses do not exist

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
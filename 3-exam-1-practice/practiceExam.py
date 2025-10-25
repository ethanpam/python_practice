def movieTicket(age):
    if age < 13:
        return 8
    elif age <= 64:
        return 12
    else:
        return 10

def convertMinutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return (f"{hours} + hours and {minutes} minutes")

def letterGrade(score):
    if score < 60:
        return "F"
    elif score <= 69:
        return "D"
    elif score <= 79:
        return "C"
    elif score <= 89:
        return "B"
    else:
        return "A"


def countVowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

def sumOddEven(n):
    total = 0
    for num in range(1,n+1):
        if num // 2 == 1:
            total = total + num
        elif num // 2 == 0:
            total = total - num
    return total
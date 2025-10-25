def creditCategory(score):
    if score <= 579:
        return "Poor"
    elif score <= 669:
        return "Fair"
    elif score <= 739:
        return "Good"
    elif score <= 799:
        return "Very Good"
    elif score >= 800:
        return "Excellent"

def main():
    score = int(input("What is your credit score?: "))
    print(creditCategory(score))

if __name__ == "__main__":
    main()
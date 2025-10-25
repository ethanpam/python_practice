def shippingCost(weight):
    if weight <= 2:
        return 10
    elif weight > 2:
        weight = weight - 2
        cost = (weight * 8) + 10
        if cost >= 25:
            return 25
        elif cost <= 25:
            return cost

def main():
    weight = int(input("Please input weight: "))
    print(shippingCost(weight))

if __name__ == "__main__":
    main()
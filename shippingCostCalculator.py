# COM S 1270 Exam #1 PRACTICE VERSION
# A) Shipping Cost Calculator

# A storage charges shipping based on package weight:
# Up to 2kg: $10
# Over 2kg: $10 + $8 per kg beyond 2
# Maximum charge: $25

# Write a function shippingCost that
# Takes one parameter, weight (the weight of the package in kg). You may assume that weight will always be a postive integer than zero
# Return the total shipping cost

# Examples:
# shippingCost(2) returns 10, because 2kg cost $10.00
# shippingCost(3) returns 18, because 3kg cost $10.00 + $8.00 = $18.00
# shippingCost(20) returns 25, because the maximum charge is $25.00

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
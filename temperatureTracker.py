# The Temperature Tracker    10-19-25      
# You are building a simple temperature analyzer for the weather station. The station collects temperatures throughout the day (in celsius) and stores them in a list

# Your job is to write a function analyzeTemps(temps) that takes a list of numbers and returns a dictionary with the following keys:
# 'max': the highest temperature recorded
# 'min': the lowest temperature recorded
# 'avg': the average temperature rounded to 1 decimal place
# 'above_avg': the count of temperatures that were above the average

# Requirements:
# Assume temps will always have at least one number
# Don't use any build-in functions that directly compute these (like statistics.mean)
# You must compute everything manually using loops, accumlators, etc

# Example:
# analyzeTemp([22.5, 25.0, 20.0, 24.5, 26.0])

# Output:
# {'max': 26.0, 'min': 20.0, 'avg': 23.6, 'above_avg: 3}

'''
This computes the given temperature list into a dictionary of the following keys:
'max': the highest temperature recorded
'min': the lowest temperature recorded
'avg': the average temperature rounded to 1 decimal place
'above_avg': the count of temperatures that were above the average

@param temps - List of temperatures given
@return - dictionary containing the following keys
'''
def analyzeTemps(temps):
    max_temp = temps[0]
    min_temp = temps[0]
    total = 0
    count = 0
    above_avg_temp = 0

    for t in temps:
        if t > max_temp:
            max_temp = t
        if t < min_temp:
            min_temp = t
        total = total + t
        count = count + 1
    avg_temp = total/count
    
    for t in temps:
        if t > avg_temp:
            above_avg_temp = above_avg_temp + 1
    
    results = {}
    results['max'] = max_temp
    results['min'] = min_temp
    results['avg'] = round(avg_temp, 1)
    results['above_avg'] = above_avg_temp
    return results

def main():
    temps = []
    n = int(input("How many temperatures (c) do you have?: "))

    for i in range(n):
        temperature = float((input(f"Enter temperature {i+1}: ")))
        temps.append(temperature)
    print(analyzeTemps(temps))

if __name__ == "__main__":
    main()
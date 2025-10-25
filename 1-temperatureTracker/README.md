The Temperature Tracker
10-19-25      

You are building a simple temperature analyzer for the weather station. The station collects temperatures throughout the day (in celsius) and stores them in a list

Your job is to write a function analyzeTemps(temps) that takes a list of numbers and returns a dictionary with the following keys:
'max': the highest temperature recorded
'min': the lowest temperature recorded
'avg': the average temperature rounded to 1 decimal place
'above_avg': the count of temperatures that were above the average

Requirements:
Assume temps will always have at least one number
Don't use any build-in functions that directly compute these (like statistics.mean)
You must compute everything manually using loops, accumlators, etc

Example:
analyzeTemp([22.5, 25.0, 20.0, 24.5, 26.0])

Output:
{'max': 26.0, 'min': 20.0, 'avg': 23.6, 'above_avg: 3}
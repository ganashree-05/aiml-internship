temperature=[22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("first reading:" ,temperature[0])
print("last reading:" ,temperature[-1])
Afternoon_peak= temperature[3:6]
print("Afternoon Peak readings:", Afternoon_peak)
last_three_hours = temperature[-3:]
print("Last 3 hours readings:", last_three_hours)
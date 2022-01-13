# loops in Python

x = 5
y = 10

# While Loop
while (x < y):
    x = x + 1
    print(x)

# for loop
for x in range(11, 15):
    print(x)

# array
_month = [
    1, "Jan",
    2, "Feb",
    3, "Mar",
    4, "May",
    5, "Apr",
    6, "Jun",
    7, "July",
    8, "Aug",
    9, "Sept",
    10, "Oct",
    11, "Nov",
    12, "Dec"
]
# printing the array
for month in _month:
    print(month)

print("\n---- Using break statement")
for month in _month:
    if (month == 4): break
    print(month)

print("\n---- Using continue statement")
for month in _month:
    if (month == 4): continue
    print(month)
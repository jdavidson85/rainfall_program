filename = 'rainfall-totals.txt'
data = []
totalRainfall = 0

infile = open(filename, 'r')

for line in infile:
    monthData = (line.strip()).split(' ')
    rainfall = monthData[1]

    rainfall = rainfall.replace('.', '')

    if rainfall.isdigit():
        monthData[1] = float(monthData[1])
        totalRainfall += monthData[1]
        data.append(monthData)
    else:
        print(f"{monthData[0]} has invalid rainfall data = {monthData[1]}")
infile.close()


avgRainfall = totalRainfall / len(monthData)


print(f"\nTotal Rainfall: {totalRainfall: .2f}")
print(f"Average Rainfall: {avgRainfall: .2f}")

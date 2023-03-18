def main():
    total = 0.0
    count = 0
    data = open("rainfall-totals.txt", "r")
    for line in data:
        line = line.rstrip("\n")
        rain = line.split()
        rain_month = rain[0]
        rain_amt = rain[1].split('.')

        if rain_amt[0].isdigit() and rain_amt[1].isdigit():
            amount = float(rain_amt[0] + "." + rain_amt[1])
            total += float(amount)
            count += 1
        else:
            print(rain_month + " does not have valid data because")
            print(str(rain[1]) + " is not a number")
    print("The total rainfall for " + str(count) + " months is " + format(total, ',.2f'))
    print("The average rainfall was " + format((total/count), ',.2f'))


main()

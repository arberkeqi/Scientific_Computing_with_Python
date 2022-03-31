def computepay(hours, rate):
    if float(hours) <= 40:
        tot_pay = float(hours) * float(rate)
        return tot_pay
    elif float(hours) > 40:
        pay = 40 * float(rate)
        extra_hours = float(hours) - 40.0
        extra_rate = float(rate) * 1.5
        extra_pay = extra_hours * extra_rate
        tot_pay1 = extra_pay + pay
        return tot_pay1 

hours = input("Enter hours: ")
rate = input("Enter rate: ")
hrs = float(hours)
rt = float(rate)
p = computepay(hrs, rt)
print("Pay", p)

hours = input("Enter hours: ")
rate = input("Enter rate: ")

if float(hours) <= 40:
    tot_pay = float(hours) * float(rate)
    print(tot_pay)
elif float(hours) > 40:
    print("Overtime!")
    pay = 40 * float(rate)
    extra_hours = float(hours) - 40.0
    extra_rate = float(rate) * 1.5
    extra_pay = extra_hours * extra_rate
    print(pay, extra_pay)
    tot_pay1 = extra_pay + pay
    print(tot_pay1)
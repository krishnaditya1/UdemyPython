total_bill=float(input())
tip=float(input())
n_friends=int(input())
print(round(total_bill*(1+tip/100)/n_friends,2))
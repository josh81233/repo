#mporting csv module 
import csv 

# csv files
payment1 = csv.reader(open("PaymentSheet.csv"))
payment2 = csv.reader(open("PaymentSheet2 (1).csv"))
f = open("combined.csv", "w")
writee = csv.writer(f)

for row in payment1:
    writee.writerow(row)
for row1 in payment2:
    writee.writerow(row1)
f.close()

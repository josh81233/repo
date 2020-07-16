import csv
import pandas as pd
df = pd.read_csv(r'combined.csv')
odnum = df['OrderNum']
sp = df['Sale Amount']
cp = df['Cost Price']
gain = sp - cp
profit = (gain/cp) * 100
com = df['Commission']
pg = df['Payment Gateway']
ppf = df['PickPack Fee']
total = com + pg + ppf
ta = df['Transferred Amount']

with open('combined.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    fields = ['Ordernum', 'profit', 'ta', 'total']


    with open('result.csv', 'w') as output:
        data = []
        csv_writer = csv.writer(output)
        data.append([odnum, profit, ta, total])
        csv_writer.writerow(fields)
        csv_writer.writerow(data)


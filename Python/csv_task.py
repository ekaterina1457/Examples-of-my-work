import csv
import collections
d = []

with open('Crimes.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    d.append(row['Primary Type'])
c = collections.Counter()
for crime in d:
  c[crime] += 1
d = dict(c)
number = 0
for i in d.items():
  if number < i[1]:
    number = i[1]
    crime = i[0]
print(crime)

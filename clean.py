import csv
from datetime import datetime

columns = []
data = []

with open("sales_data.csv", "rb") as dataFile:
	csvReader = csv.reader(dataFile)

	columns = csvReader.next()

	for row in csvReader:
		data.append(row)

for row in data:
	dateObject = ""

	if("-" in row[5]):
		dateObject = datetime.strptime(row[5], "%m-%d-%Y %H:%M")
	else:
		dateObject = datetime.strptime(row[5], "%m/%d/%Y %H:%M")

	row[5] = dateObject.strftime("%Y") + "-" + dateObject.strftime("%m") + "-" + dateObject.strftime("%d")


with open("clean_data.csv", "wb") as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(columns)
	csvWriter.writerows(data)
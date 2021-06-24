import csv

columns = []
data = []

with open("clean_data.csv", "rb") as dataFile:
	csvReader = csv.reader(dataFile)

	columns = csvReader.next()

	for row in csvReader:
		data.append(row)


# creating csv file for table 'order'

orderRows = []
count = 0

for row in data:
	count += 1
	orderRows.append([count, row[0], row[1], row[2], row[3], row[4], row[6], row[24]])
	

with open("order.csv", "wb") as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(["Order ID", "Order Number", "Quantity", "Price", "Line Number", "Sales", "Status", "Deal Size"])
	csvWriter.writerows(orderRows)



# creating csv file for table 'date'

dateRows = []
uniqueItems = []
count = 0

for row in data:
	temp = [row[5], row[7], row[8], row[9]]
	if temp not in uniqueItems:
		count += 1
		dateRows.append([count, row[5], row[7], row[8], row[9]])
		uniqueItems.append(temp)

with open("date.csv", "wb") as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(["Date ID", "Date", "Quarter", "Month", "Year"])
	csvWriter.writerows(dateRows)



# creating csv file for table 'product'

productRows = []
uniqueItems = []
count = 0

for row in data:
	temp = [row[10], row[11], row[12]]
	if temp not in uniqueItems:
		count += 1
		productRows.append([count, row[10], row[11], row[12]])
		uniqueItems.append(temp)

with open("product.csv", "wb") as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(["Product ID", "Product Line", "MSRP", "Product Code"])
	csvWriter.writerows(productRows)



# creating csv file for table 'customer'

customerRows = []
uniqueItems = []
count = 0

for row in data:
	temp = [row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23]]
	if temp not in uniqueItems:
		count += 1
		customerRows.append([count, row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23]])
		uniqueItems.append(temp)

with open("customer.csv", "wb") as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(["Customer ID", "Name", "Phone", "Address 1", "Address 2", "City", "State", "Postal Code", "Country", "Territory", "Contact Last Name", "Contact First Name"])
	csvWriter.writerows(customerRows)


# creating csv file for fact table

factRows = []
count = 0

for row in data:
	temp = [0,0,0,0]
	count += 1
	
	temp[0] = count
	
	for obj in dateRows:
		if(row[5] == obj[1] and row[7] == obj[2] and row[8] == obj[3] and row[9] == obj[4]):
			temp[1] = obj[0]

	for obj in productRows:
		if(row[10] == obj[1] and row[11] == obj[2] and row[12] == obj[3]):
			temp[2] = obj[0]

	for obj in customerRows:
		if(row[13] == obj[1] and row[14] == obj[2] and row[15] == obj[3] and row[16] == obj[4] and row[17] == obj[5] and row[18] == obj[6] and row[19] == obj[7] and row[20] == obj[8] and row[21] == obj[9] and row[22] == obj[10] and row[23] == obj[11]):
			temp[3] = obj[0]

	factRows.append(temp)


with open("fact_table.csv", "wb") as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(["Order ID", "Date ID", "Product ID", "Customer ID"])
	csvWriter.writerows(factRows)

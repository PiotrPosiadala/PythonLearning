import csv
    
with open('c:/temp/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    for row in csvreader:
#        print('|'.join(row))
    while True:
        try:
            data = next(csvreader)
            print(data)
        except StopIteration:
            break
    print('All data was processed')
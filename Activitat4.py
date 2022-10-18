import csv 
with open("cars_data.csv",newline='') as csvFile:
    render = csv.reader(csvFile)
    for row in render:
        print(row)
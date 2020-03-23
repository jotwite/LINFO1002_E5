
import numpy as np
import csv

with open("total_deaths.csv") as file:
    reader = csv.reader(file)
    full_data = list(list(rec) for rec in csv.reader(file, delimiter=','))
    file.close()  # close the csv




with open("totaldeaths.txt","w") as file:
    for data in full_data:
        file.write(str(data)+"\n")
    
        

import numpy as np
import csv

with open("full_data.csv") as file:
    reader = csv.reader(file)
    full_data = list(list(rec) for rec in csv.reader(file, delimiter=','))
    file.close()  # close the csv





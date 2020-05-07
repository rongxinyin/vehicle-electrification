import pandas as pd
import model
import csv

class Vehicle(object):
    def __init__(self, var1, var2, var3)
        self.name = var1
        self.age = var2
        self.hobbies = var3

vehicle_list = []

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        vehicle_list.append(myClass(row[0], row[1], row[2:]))

dt = pd.read_csv('data/vehicle_model.csv', index_col=0)
print(dt)
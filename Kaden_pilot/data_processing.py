
import numpy as np

import csv
with open('reproduction.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row))


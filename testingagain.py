
import csv

with open('user.csv', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    print(last_line)
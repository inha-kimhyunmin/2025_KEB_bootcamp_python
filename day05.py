import random
import csv

try:
    with open("students.csv", 'r') as fp:
        students_list = fp.readlines()
        print(students_list)

except FileNotFoundError as err:
    print(f"{err}")
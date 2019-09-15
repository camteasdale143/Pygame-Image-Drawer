
import pygame
import csv

colors = []
def hex_to_rgb(hex):
     hex = hex.lstrip('#')
     return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

f = open("list2.csv", "a")

with open('color.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row[0])
        f.write("{0},{1}\n".format(hex_to_rgb(row[0]),row[1]))
f.close()




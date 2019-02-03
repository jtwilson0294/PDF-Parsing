import csv
import json
import io
import os
import ast

PATH = "your/path/here"

operating_dict = json.load(open(PATH + "PDF_Dict.txt"))

with open('WPs.csv', 'w', newline='') as csvfile:
    wp_writer = csv.writer(csvfile, delimiter=',',
                           quotechar="'", quoting=csv.QUOTE_MINIMAL)
    for key, value in operating_dict.items():
        wp_writer.writerow([key.encode('utf-8'), value.encode('utf-8')])

# test
# print(operating_dict['Zenome'].encode('utf-8'))

# TODO strip keys and values of all special characters ex. (),'" and newlines

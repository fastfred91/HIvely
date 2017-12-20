#!/usr/bin/env python

import csv


#Pulls data to console from the downloaded csv

NON_PS_SUPPORT_REPS = (['Grey Elerson', 'Stefan Nychka', 'Eddie Hsu',
                        'Zach Cowart', 'Robert Babcock', 'Brittany Luttrell'])


def read_csv_data():
    with open('/Users/freddycastro/Documents/csv/hively.csv', 'r') as f:
        reader = csv.reader(f)
        hively_list = list(reader)
        return hively_list


def create_list_of_lists(hively_list):
    hively_data = []
    hively_data.append(['Rating', 'Points', 'From', 'Comment', 'Created', 'Ticket'])
    for item in hively_list:
        hively_row = []
        if item[4] == 'Points' or item[0] in NON_PS_SUPPORT_REPS:
            continue
        else:
            hively_row.append(item[3])
            hively_row.append(item[4])
            hively_row.append(item[7])
            hively_row.append(item[8])
            hively_row.append(item[9][:10])
            hively_row.append(item[13])
            hively_data.append(hively_row)
    return hively_data


def create_new_file(hively_data):
    with open('/Users/freddycastro/Documents/csv/hively-data.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(hively_data)

hively_list = read_csv_data()
hively_data = create_list_of_lists(hively_list)
create_new_file(hively_data)


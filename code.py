#------------------------------------------------
#
#     Formatage Fichier CSV
#
#      UED - Deep Learning
#
#       Authors :
#   -Théo CHASSANITE
#
#------------------------------------------------

import csv
import time
import sys
from datetime import datetime
from datetime import timedelta
    #------------------------------------------------------#
    # Part that define the name of the output file         #
    #------------------------------------------------------#
py3 = sys.version_info[0] > 2 #creates boolean value for test that Python major version > 2
if py3:
  file_name = input("Please enter your file name: ") + ".csv"
else:
  sys.exit("  Error : this script works with pyhton 3.\n  Please update your version of python.")

file_byte = open("bitcoin-historical-data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv","r")
reader_byte = csv.reader(file_byte)
writer = csv.writer(open(file_name, "w"))

total_row = 2099761
'''
print(total_row)
total_row = len(list(reader))
total_row = reader.line_num
print(total_row)
total_row = csv.field_size_limit(sys.maxsize)
print(total_row)
'''
    #--------------------------------------------------------#
    # Part that define the basic variables and set the shell #
    #--------------------------------------------------------#
row_validity = True
number_row = 0
print("Creation of the dataset")
print("\r   [%d" %0 + "%]" + " |•••••••••••••••••••••••••|", end='\r')
header = next(reader_byte)
last_sample = datetime.fromtimestamp(0)
    #------------------------------------------------------#
    # Part that rewrite new data                           #
    #------------------------------------------------------#
for row in reader_byte :
    number_row +=1
    dt_object = datetime.fromtimestamp(int(row[0]))
    if last_sample <= dt_object :
        last_sample = dt_object + timedelta(minutes=5)
        for data in row :
            if data == 'NaN' :
                row_validity = False
        if row_validity :
            ts = time.gmtime(int(row[0]))
            writer.writerow([time.strftime("%x %X", ts), row[1], row[2], row[4], row[5], row[6], row[7]])
        row_validity = True
    number = int((number_row / total_row)*100)
    print("\r   [%d" %number + "%]" + "|" + "=" * int(number/4) + ">" + "•" * (24-int(number/4)) + "|  " + str(number_row) + "/" + str(total_row), end='\r')
    #------------------------------------------------------#
    # Part that print the final state of the shell         #
    #------------------------------------------------------#
print("\r   [%d" %100 + "%]" + "|" + "=" * 25 + "|")
print("Successfully created the dataset : " + file_name)

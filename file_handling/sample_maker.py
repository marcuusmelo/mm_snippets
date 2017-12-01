import csv
import operator
from datetime import date
import os
from itertools import islice
import os.path
from itertools import islice

#
# DESCRIPTION
# Read the files of a specified file type in the directory
# and write a sample of it with the first rows according
# to what specified in sample_size
# Key topics: read csv, write csv, file iterator
#

file_type = '.txt'
sample_size = 50

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(file_type)]:
        today = date.today()
        file_name = filename[0:-4]
        # First, open and read the file that will be imported
        with open(file_name + file_type) as myfile:
            head = list(islice(myfile, sample_size))
        # Fix the NUL bytes
        with open(file_name + '_sample' + file_type, 'wb') as new_file:
        for row in head:
            new_file.write(row.replace('\x00', ''))
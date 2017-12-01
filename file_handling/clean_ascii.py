import time
import csv
import operator
from datetime import date
import os
from itertools import islice
import os.path

#
# DESCRIPTION
# This code will read the csv files in a directory
# clean the non ascii elements from it, and write it in
# a new file at a subdir clean/
# Key topics: read csv, write csv, file iterator, 
# row iterator, non ascii chars, timer.
#


start_time = time.time()
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".csv")]:
        path = dirpath
        file_name = filename[0:-4]
    	# Open and read the file that contains the data
        f_ecl = open(path + '/' + file_name + '.csv')
        f_ecl_c = open('../clean/' + file_name +'.csv', 'a')
        writer_clean = csv.writer(f_ecl_c, delimiter = ',')
        # Declare the vector
        main_ecl_row = [['' for x in range(200)] for x in range(1)]
        # Declare the progress variables
        exit_flag = 0 
        read_start = 0
        # Loop, read and write the files 
        row_number = 0 
        while exit_flag == 0:
            file_sec = list(islice(f_ecl, 0, 1, 1))
            file_main_ecl_row = csv.reader(file_sec, delimiter = ',')
            read_n_row = 0
            for row in file_main_ecl_row:
                read_n_row = 1
                for c in range(len(row)):
                    cell = ''.join([x for x in row[c] if ord(x)<128])
                    main_ecl_row[0][c] = cell
                c = c + 1
                writer_clean.writerows(main_ecl_row)
                read_start = read_start + 1
                print str(read_start) + ' rows read'
            if read_n_row == 0:
                exit_flag = 1
                break

print("--- %s seconds ---" % (time.time() - start_time))
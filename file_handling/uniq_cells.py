
import os
import csv
import pandas as pd

#
# DESCRIPTION
# This code reads a csv files inside the current directory
# and write a new file with the unique cells for each file.
# Also, you can use this to find specific sets of unique cells
# in this case I was looking for unique cells that had some
# specific pieces of string in each (lines 33 to 38)
#

# Get files to examine
info_dir = '.'

# Get list of files

files = os.listdir(info_dir)

# only csv files
files = [x for x in files if x[-3:] == 'csv']

for csvfile in files:
    unique_cells_list = []
    df = pd.read_csv(os.path.join(info_dir, csvfile))
    df_list = df[df.keys()].values.tolist()
    for row in df_list:
        for cell in row:
            if str(cell) != 'nan':
                if isinstance(cell, str):
                    lower_cell = cell.lower()
                    if cell not in unique_cells_list:
                        if ('date_init' in lower_cell) \
                        or ('date_end' in lower_cell) \
                        or ('total_value' in lower_cell):
                            unique_cells_list.append(cell)
    unique_cells = []
    for x in unique_cells_list:
        unique_cells.append([x])
    f_uc = open('uc_' + csvfile, 'wb')
    writer_fuc = csv.writer(f_uc, delimiter = ',')
    writer_fuc.writerows(unique_cells)
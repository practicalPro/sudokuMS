import csv
import sys
import time
import os

while 1:
    lvl = input("Please enter number of difficulty from 1-8 or stop: ")
    f=open(os.path.join(sys.path[0],"pipe.txt"),"r+")
    f.seek(0)
    f.truncate()
    f.write(lvl)
    f.close()
    if(lvl!="stop" and lvl.isdigit() and int(lvl)in range(1,9)):
        sudoku_grid = []
        with open('input.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                sudoku_grid.append(row)
        print ("unprocessed:\n",sudoku_grid)
        time.sleep(2)
        result_grid = []
        with open('output.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                result_grid.append(row)
        print ("processed:\n",result_grid)
    elif (lvl=="stop"):
        break
    



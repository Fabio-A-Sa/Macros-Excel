# Modules

import os
import shutil
from string import ascii_letters as abc

# Functions

def search ():

    pwd = os.getcwd()
    enable_plugs = [letter for letter in abc.upper()]
    ways = ["{}:\Garmin\geocache_visits.txt".format(plug) for plug in enable_plugs]
    pointer = False
    counter = 0

    while (pointer != True and counter < len(ways)):
        
        field_note = ways[counter]

        try:
            shutil.copy(field_note, pwd)
            pointer = pointer or True
            return export ()

        except FileNotFoundError:
            error = "Directory {} cannot be found".format(field_note)
            print(error)

            pointer = pointer and True
            counter = counter + 1
            continue
    
    main_error = "GPS is not connected"
    print (main_error)
    return None


def export ():
    
    import xlwt
    from xlwt import Workbook
    from datetime import datetime

    current_day = datetime.now()
    date = current_day.strftime("%Y-%m-%d")
    wb = Workbook()
    Excel = wb.add_sheet(date)
    os.rename("geocache_visits.txt", "drafts.txt")
    drafts = open("drafts.txt", "r+") # Read and paste

    DATA = drafts.readlines()
    top = "Cache Date Hour Found? Notes".strip().split(" ")

    y = 0
    for flag in range(len(top)):
        Excel.write(y, flag, top[flag])

    y = 1
    for log in DATA:

        log = log[:6] + (log[6:]).replace("T", ",").replace("Z", "")
        items = log.split(",")

        x = 0
        for item in items:
            Excel.write(y, x, item)
            x += 1

        y += 1

    wb.save("Logs " + date + ".xls")
    drafts.close()
    os.remove("drafts.txt")


if __name__ == "__main__":
    search ()

#!/usr/bin/env python

__author__ = "Jani Päijänen"
__copyright__ = "Copyright 2015, Jani Päijänen. All rights reserved"
__license__ = "New BSD License"
__version__ = "0.0.1"
__email__ = "jani dot paijanen+distinctcsv at gmail dot com "
__status__ = "Production"



import argparse
from readercsv import *

class Dummy():
    pass

def csv_reader(filename, empty_cols, column_title_max_length):
    all_cols = Dummy()
    all_cols.uv = []
    max_rows = 0

    max_empty_cols = empty_cols

    with open(filename) as f:
        empty_col = 0

        for colnum in range(0, 1000):
            col_txt = []
            col_total = 0
            prev_col = -1

            col_info = Dummy()
            col_info.empty = True

            for (rownum,col,txt) in read_stream_csv_col(f, colnum):
                if rownum > max_rows:
                    max_rows = rownum

                try:
                    txt = txt.strip()
                except Exception:
                    pass

                if (txt is not None and txt != ""):
                    col_total = col_total +1

                    if (col_info.empty == True):
                        #print("{0} empty = False".format(colnum))
                        col_info.empty = False

                    if txt not in col_txt:
                        col_txt.append(txt)

            if col_info.empty == True:
                empty_col = empty_col +1
                #print("{0} empty == True".format(colnum))
            else:
                empty_col = 0

            # print column contents
            #if col_txt[0] == "Deleted":
            #    print (col_txt)
            #    #for c in col_txt:
            #    #    print ("{0}".format(c))
            #    print ("length {0}".format (len(col_txt)) )
            #    break
            # print number of unique items
            try:
                #print ("{0}:{1} ".format(col_txt[0], len(col_txt)-1))
                #{'name' : 'Al Pacino',

                all_cols.uv.append ( dict([(col_txt[0], "{0}/{1}".format(len(col_txt)-1, col_total-1))]) )

            except Exception as e:
                #print (e)
                #print ("{0}:0".format(colnum))
                pass

            # if enough empty columns then break
            if empty_col >= max_empty_cols:
                all_cols.uv = all_cols.uv[ :len(all_cols.uv)-max_empty_cols ]

                break

        print ("Field:unique values/total values/rows\n-------------------")
        for i in all_cols.uv:
            for k,v in i.items():
                print ("{0}:{1}/{2}".format(k[:column_title_max_length],v,max_rows))


def main():
    parser = argparse.ArgumentParser(description="Count non-empty, non-whitespace unique items.")
    parser.add_argument("filename", help="Filename to read (csv).",
                type=str)

    parser.add_argument("-e", "--empty_cols", help="break after # of empty columns.",
                    type=int, default=2)

    parser.add_argument("-c", "--column_title_max_length", help="max # of chars to print from a column_title.",
                    type=int, default=128)

    args = parser.parse_args()
    csv_reader (args.filename, args.empty_cols, args.column_title_max_length)

if __name__ == '__main__':
    main()

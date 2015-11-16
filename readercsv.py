#!/usr/bin/env python
# python3
import os
import sys
import csv


__author__ = "Jani Päijänen"
__copyright__ = "Copyright 2015, Jani Päijänen. All rights reserved"
__license__ = "New BSD License"
__version__ = "0.0.1"
__email__ = "jani dot paijanen+testreader at gmail dot com "
__status__ = "Testing"



def read_stream_csv_row(stream, rows_to_skip=0, enc="iso-8859-1", newline='', delim=";", quote='"'):

    reader = csv.reader(stream, delimiter=delim, quotechar=quote)
    rows = 0
    for rownum, row in enumerate(reader):
        if rows < rows_to_skip:
            rows += 1
            continue
        #logger.debug (row)
        txt = ""
        try:
            txt = str(row).strip()
        except Exception:
            pass

        yield (rownum,txt)


def read_stream_csv_col(stream, col=0, rows_to_skip=0, enc="iso-8859-1", newline='', delim=";", quote='"'):

    stream.seek(0)
    reader = csv.reader(stream, delimiter=delim, quotechar=quote)
    rows = 0
    for rownum, row in enumerate(reader):
        if rows < rows_to_skip:
            rows += 1
            continue
        #logger.debug (row)
        txt = ""
        try:
            txt = str(row[col]).strip()
        except Exception:
            pass

        yield (rownum,col,txt)


def read_csv_col(filename, col=0, rows_to_skip=0, enc="iso-8859-1", newline='', delim=";", quote='"'):
    retval=[]
    with open(filename, newline=newline, encoding=enc) as f:
        read_csv_stream(f)

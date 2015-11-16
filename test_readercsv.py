#!/usr/bin/env python


__author__ = "Jani Päijänen"
__copyright__ = "Copyright 2015, Jani Päijänen. All rights reserved"
__license__ = "New BSD License"
__version__ = "0.0.1"
__email__ = "jani dot paijanen+testreader at gmail dot com "
__status__ = "Testing"

"""
Copyright (C) 2015 Sparta Consulting Oy. All rights reserved.
Authors: jp
"""

from readercsv import *

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def test1():

    output = StringIO()
    output.write('name;company;title;dob\n')
    output.write('Donald;Acme;The Unlucky Duck;1928\n')
    output.write('Scrooge;Acme;Uncle;1928\n')
    output.write('Mickey;Acme;Mouse;1928\n')
    output.write('Hedgehog;Sega;The game;1987\n')

    #print (output.getvalue())
    output.seek(0)
    for index,(row,col,item) in enumerate(read_stream_csv_col(output, 0, 0, "utf-8")):
        e = ["name","Donald","Scrooge","Mickey","Hedgehog"][index]
        #print (e, item)
        assert(item == e)

    output.seek(0)
    for index,(row,col,item) in enumerate(read_stream_csv_col(output, 0, 1, "utf-8", )):
        e = ["Donald","Scrooge","Mickey","Hedgehog"][index]
        #print (e, item)
        assert(item == e)


    output.seek(0)
    for index,(row,item) in enumerate(read_stream_csv_row(output, 0, "utf-8", )):
        #e = ["Donald","Scrooge","Mickey","Hedgehog"][index]
        print (item)
        #assert(item == e)

def main():
    test1()

if __name__ == '__main__':
    main()

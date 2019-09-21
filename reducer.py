# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 04:16:44 2019

@author: rkrishnan
"""

import sys

def reducer():
    salesTotal = 0
    oldKey = None
    
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            # Something has gone wrong. Skip this line.
            continue
    
        thisKey, thisSale = data
        if oldKey and oldKey != thisKey :
          print(oldKey, "\t", salesTotal)
          oldKey = thisKey
          salesTotal = 0
    
        oldKey = thisKey
        try:
            float(thisSale)
        except ValueError:
            thisSale=0
        #print(type(thisSale))
        #if type(thisSale)=="int" or type(thisSale)=="float":
        salesTotal += float(thisSale)
    
    if oldKey != None:
        print(oldKey, "\t", salesTotal)

test_text = """Miami\t99.95
Miami\t99.95
New York\t9.50
Miami\t99.95
khjkhkhjhkh
jjhkh\tjkjhkj"""

# This function allows you to test the mapper with the provided test string
def main():
	from io import StringIO
	sys.stdin = StringIO(test_text)
	reducer()
	sys.stdin = sys.__stdin__
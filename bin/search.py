#!/usr/bin/env python
import six
import sys
import codecs
import argparse
import uecsyllabus

if six.PY2:
    sys.stdout = codecs.getwriter("utf_8")(sys.stdout)

parser = argparse.ArgumentParser(description="Search UEC syllabus")
parser.add_argument("--course", required=True, help="Course ID")
parser.add_argument("--year", required=True)
parser.add_argument("--grade", required=True)


args = parser.parse_args()
finder = uecsyllabus.Finder()
result = finder.search(vars(args))
for row in result:
    sys.stdout.write(("\t".join(row) + "\n"))

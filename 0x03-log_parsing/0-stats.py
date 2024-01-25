#!/usr/bin/python3
"""
Log parsing files
"""
import sys
import re

status_codes = {}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        match = re.search(
            r'(\S+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match is not None:
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
            total_size += file_size
        line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                print("{}: {}".format(code, status_codes[code]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

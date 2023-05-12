#!/usr/bin/env python3

import sys
import signal

# Define the possible status codes
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize the metrics
total_file_size = 0
line_counts = {code: 0 for code in STATUS_CODES}

# Define the signal handler to print the statistics on interrupt
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Set the signal handler for interrupt
signal.signal(signal.SIGINT, signal_handler)

# Define a function to print the statistics
def print_stats():
    print(f'Total file size: {total_file_size}')
    for code in sorted(line_counts):
        count = line_counts[code]
        if count > 0:
            print(f'{code}: {count}')

# Read stdin line by line and update the metrics
line_num = 0
for line in sys.stdin:
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[8])
        file_size = int(parts[9])
        if status_code in STATUS_CODES:
            total_file_size += file_size
            line_counts[status_code] += 1
            line_num += 1
            # Print the statistics every 10 lines
            if line_num % 10 == 0:
                print_stats()
    except (ValueError, IndexError):
        pass


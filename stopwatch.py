#! python3
# stopwatch.py - a stopwatch

import time


# Display instructions
print("Press 'Enter' to begin, then press 'Enter' to lap the stopwatch")
print("Press Ctrl-C to quit")

input()     # User inputs 'enter'
print("Started...")
start_time = time.time()
end_time = start_time

lap_num = 1

# Start tracking lap times

try:
    while True:
        input()
        laptime = round(time.time() - end_time, 2)
        total_time = round(time.time() - start_time, 2)
        print("Lap #%s: %s (%s)" % (lap_num, total_time, laptime), end='')
        print("\n")
        lap_num += 1
        end_time = time.time()    # reset the last lap time

except KeyboardInterrupt:
    # Handle the keyboard intterupt gracefully with a print-out
    print('Done.')


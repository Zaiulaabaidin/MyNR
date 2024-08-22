import time

# Infinite loop to keep printing the current time every 10 seconds
while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Current Time:", current_time)
    time.sleep(10)

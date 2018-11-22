from commons.utils import Utils
import time


def dates_message(message, line='start'):
    Utils.print_message(" Date =========> {0} ".format(message), line=line)


# localtime
dates_message("localtime")
localtime = time.localtime(time.time())
print("Current time is: ", localtime)
dates_message("localtime", "end")

# formatted time
dates_message("formatted time")
localtime = time.asctime(time.localtime(time.time()))
print("Formatted Time", localtime)
dates_message("formatted time", "end")

# Print Time
dates_message("Print Current Time")
print("Current Time ", time.time())
dates_message("Print Current Time", "end")


# Print ASCII Time
dates_message("Ascii Time")
t = time.localtime()
print(time.asctime(t))
dates_message("Ascii Time", "end")

# sleep
dates_message("sleep")
print(time.asctime(time.localtime(time.time())))
time.sleep(10)
print(time.asctime(time.localtime(time.time())))
dates_message("sleep", "end")

# strptime
dates_message("strptime")
timerequired = time.strptime("26 Jun 14", "%d %b %y")
print(timerequired)
dates_message("strptime", "end")


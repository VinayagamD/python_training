from commons.utils import Utils
import time


def dates_message(message, line='start'):
    Utils.print_message(" Date =========> {0} ".format(message), line=line)


# localtime
Utils.print_message("localtime")
localtime = time.localtime(time.time())
print("Current time is: ", localtime)
Utils.print_message("localtime", "end")

# formatted time
Utils.print_message("formatted time")
localtime = time.asctime(time.localtime(time.time()))
print("Formatted Time", localtime)
Utils.print_message("formatted time", "end")

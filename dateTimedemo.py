from datetime import datetime

current_date = datetime.today().date()  #Gets the current date
current_time = datetime.today().time()
currdatetime = datetime.today()  #Gets date and time
print(current_date)
print(current_time)
print(currdatetime)

filename = currdatetime.strftime('%Y-%m-%d-%H-%M-%S-%f')

## This is mostly required for filenaming and recording the timestamps
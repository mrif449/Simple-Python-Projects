import winsound
import time
def countdown(timer):
    while timer:
        min, sec = divmod(timer,60)
        alarm = "{:02d}:{:02d}".format(min,sec)
        print(alarm,end="\r")
        time.sleep(1)
        timer -= 1
timer = int(input("Enter the time in second(s): "))
countdown(timer)
for x in range(10000):
    winsound.PlaySound("alarms",winsound.SND_FILENAME)
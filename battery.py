from pynotifier import Notification
import psutil

battery = psutil.sensors_battery()
percent = battery.percent

Notification(
    title="Battery Percentage", 
    description= str(percent)+ "%percent remaning!",
    duration=10
).send()
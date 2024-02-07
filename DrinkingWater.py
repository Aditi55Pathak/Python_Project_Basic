from plyer import notification
import time


def show_noti(title, message):
    time.sleep(5)
    notification.notify(title=title, message=message, app_icon=None, timeout=10)


show_noti(
    "Paaniii Pilooo",
    "You are hence reminded to drink water bub.",
)

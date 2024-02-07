import time

from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(

            title='======> Time to take your medicines <======',
            message="Hey! Its time to have your medicines. Properly Eat them. No one is watching,but God is",
            timeout=10

        )
        time.sleep(5)

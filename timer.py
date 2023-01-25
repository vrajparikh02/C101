import time
def countdown_timer(secends):
    while secends>0:
        mins=int(secends/60)
        secs=int(secends%60)
        if secs>=10:
            timer=f'{mins}:{secs}'
        else:
            timer=f'{mins}:0{secs}'
        print(timer,end='\r')
        time.sleep(1)
        secends-=1
    print('times up')
secends=int(input("Enter time in Secends: "))
countdown_timer(secends)
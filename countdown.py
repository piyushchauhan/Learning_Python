#! python3
# countdown.py - A simple countdown script.
import subprocess
import time
import sys

# string variable is a prompt message
string = '''
To exit press ENTER. 
To restart with new time type the time and then press ENTER'''

if len(sys.argv) > 1:
    # Take Time from cmd line
    try:
        timeLeft = float(sys.argv[1]) * 60
        print('The entered time is cmd line is', round(timeLeft / 60), 'minutes')
    except ValueError:
        # Default Time is 20 min
        timeLeft = 60 * 20
else:
    # Default Time is 20 min
    timeLeft = 60 * 20

while True:
    print('Counter started for %s minutes' % round(timeLeft / 60, 2))
    while timeLeft > 0:
        print(timeLeft, end='\t', flush=True)
        time.sleep(1)
        timeLeft = timeLeft - 1

    # At the end of the countdown, play a sound file.
    playFile = subprocess.Popen(['start', 'alarm.wav'], shell=True)
    print(string)
    a = input()
    if not a:
        print('Thank You for using the countdown timer.')
        time.sleep(2)
        break
    else:
        try:
            timeLeft = float(a) * 60
        except ValueError:
            try:
                # Get timeLeft from
                timeLeft = float(sys.argv[1]) * 60
            except:
                timeLeft = 60 * 20
        continue
sys.exit()

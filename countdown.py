# Simple countdown script

import time, subprocess # Import 'time' and 'subprocess module'

timeLeft = 2
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1
print(0) # End the countdown at zero

# Play a Sound and  at the end of the countdown
subprocess.Popen(['start', 'alarm.wav'], shell=True)

# Print message onto the screen
print(f"\nTIME IS UP!!!")





from gpiozero import Button
import time

button = Button(2)

button.wait_for_press()
t1 = time.time()
print "Timer Started: " + str(t1) + " - press in 2 seconds"
button.wait_for_release()
button.wait_for_press()
t2 = time.time()
print t2
print "Interval = " + str(t2-t1) + " seconds"

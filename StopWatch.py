import time
import datetime

def stopwatch() :
   # Display the program's instructions.
   print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
   input()                    # press Enter to begin
   print('Started.')
   startTime = time.time()    # get the first lap's start time
   lastTime = startTime
   lapNum = 1
      
      # Start tracking the lap times.
   try:
      while True:
         totalTime = round(time.time() - startTime, 2)
         print(totalTime, end='\r')
   except KeyboardInterrupt:
         # Handle the Ctrl-C exception to keep its error message from displaying.
         txt = str(datetime.timedelta(seconds=round(totalTime)))

         # spilt string
         x = txt.split(":")

         printOut = x[0] + " hours " + x[1] + " mins " + x[2] + " secs "
         
         print(printOut)

         print('\nDone.')

         return totalTime
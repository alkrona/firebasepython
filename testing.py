import time
import esp32testing
data1=000
data2=111
present_time = time.time()
sleeping_time=.1
while(present_time + 130>time.time()):
   esp32testing.firesender(data1)
   time.sleep(sleeping_time)
   esp32testing.firesender(data2)
   time.sleep(sleeping_time) 

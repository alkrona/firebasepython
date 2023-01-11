import time
import main
data1="0000000000000000"
data2="1111111111111111"
present_time = time.time()
sleeping_time=.1
while(present_time + 130>time.time()):
   main.firesender(data1)
   time.sleep(sleeping_time)
   main.firesender(data2)
   time.sleep(sleeping_time) 

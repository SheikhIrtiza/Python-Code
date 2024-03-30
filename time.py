# import time

# start = time.time()
# for i in range(1, 101):
#     print(i)
    
# print(time.time() - start)
# another implementation

import time
start = time.time()
i = 1 
while i<101:
    print(i)
    i+=1
    
print(time.time() - start)
# problems with this approach
# different time for different algorithm  
# time varies if implementation changes
# different machines different time
# does not work for extremely small input
# time varies for different inputs, but can't establish a relationship

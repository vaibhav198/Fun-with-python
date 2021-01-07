#We'll see how print statement affect the execution time
import time
a =0
#Running a for loop in which we'll print i
t1 = time.time()
for i in range(13):
    a = a+i
    print("index: ", i)
T1 = time.time() - t1
print("t1: ", T1)
#Running the same for loop in which we'll not print anything
t2 = time.time()
for i in range(13):
    a = a + i
T2 = time.time() - t2
print("t2: ", T2)
print("Diff: ", T1-T2)
print("Compare: ", T1/T2)

import numpy as np
import time

x_arr = np.array([[1,0], [1,1], [1,2], [1,3]])
y_arr = np.array([[0], [1], [4], [9]])

total = 0
for i  in range(10):
  start_time = time.time()
  x_inv = np.linalg.pinv(x_arr)
  end_results = np.dot(x_inv, y_arr)
  total += (time.time() - start_time)
  print(end_results)

print("Average Time in Python: ",total/10)

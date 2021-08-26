import time

def sum_of_a_million():
  start = time.time()
  result = 0
  for i in range(1,1000000):
    result += i
  end = time.time()
  return end-start

sum_times = 0
for i in range(1,10):
  result = sum_of_a_million()
  sum_times += result
print("\nAverage Time in Python:", sum_times/10)

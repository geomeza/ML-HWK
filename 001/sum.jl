tfunction sum_of_a_million()
  sum = 0
  for i in 1:1000000
    sum += i
  end
  return sum
end

total = 0
for i in 1:10
  global total
  start = time_ns()
  sum_mill = sum_of_a_million()
  total += (time_ns() - start)
end
println("Average Time in Julia: ",total/10000000000)



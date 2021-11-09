using LinearAlgebra

x_arr = [1 0; 1 1; 1 2; 1 3;]
y_arr = [0; 1; 4; 9;]

global total = 0
for i  in 1:10
  global total
  start_time = time_ns()
  x_inv = pinv(x_arr)
  end_results = x_inv * y_arr
  total += (time_ns() - start_time)
  println(end_results)
end

println("Average Time in Julia: ",total/10000000000)

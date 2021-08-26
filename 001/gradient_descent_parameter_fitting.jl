function central_difference(f, points, h)
  results = []
  for i in 1:length(points)
    points_forward = map(x -> x, points)
    points_forward = replace(points_forward, points_forward[i] => points_forward[i] + h)

    points_backward = map(x -> x, points)
    points_backward = replace(points_backward, points_backward[i] => points_backward[i] - h)
    result = (f(points_forward...) - f(points_backward...))/ (2*h)
    append!(results, result)
  end
  return results
end

descent_function(a,b) = (a)^2 + (a+b-1)^2 + (a+2*b-2)^2

function descend(f, points, h, alpha)
  derivatives = central_difference(f, points, h)
  new_points = []
  for i in 1:length(points)
    new_point = points[i] - alpha*derivatives[i]
    append!(new_points, new_point)
  end
  return new_points
end



start = time_ns()
for i in 1:10
  points = [0,2]
  for i in 1:2
    points = descend(descent_function, points, 0.1, 0.001)
    print(points)
  end
end

print("Average time in Julia: ", (time_ns()-start)/10000000000)

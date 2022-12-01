using DelimitedFiles

data = readdlm("input.txt", '\n', Int32)
println(count(diff(data[:]) .> 0))
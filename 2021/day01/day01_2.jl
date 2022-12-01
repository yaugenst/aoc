using DelimitedFiles
using DSP

data = readdlm("input.txt", '\n', Int32)
sliding = conv(data, ones(3))
println(count(diff(sliding[3:end-2]) .> 0))
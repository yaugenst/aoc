using DelimitedFiles

function bits_to_int(bits)
    return sum(bits .* (2 .^ collect(length(bits)-1:-1:0)))
end

function criteria(bits, crit)
    crit
end

function main()
    data = readdlm("input.txt", '\n', String)
    m = vcat([parse.(Bool, hcat(d...)) for d in data]...)
    most_common = mapslices(x -> sum(x) / length(x), m, dims=1)' .> 0.5
    criteria(m, most_common)
end

main()
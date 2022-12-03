function priority(x)
    return islowercase(x) ? x - 'a' + 1 : x - 'A' + 27
end

function part1(data)
    p = 0
    for line in data
        s = length(line) ÷ 2
        a, b = line[1:s], line[end-s+1:end]
        p += priority(only(a ∩ b))
    end
    return p
end

function part2(data)
    p = 0
    for row in eachcol(reshape(data, (3, :)))
        p += priority(only(intersect(row...)))
    end
    return p
end

function main()
    data = filter(x -> !isempty(x), split(readchomp("input.txt"), "\n"))
    @show part1(data)
    @show part2(data)
end

main()
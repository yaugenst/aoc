function main()
    data = (filter(x -> !isempty(x), split(x, "\n")) for x in split(readchomp("input.txt"), "\n\n"))
    cal = [sum(map(x -> parse(Int, x), line)) for line in data]
    @show maximum(cal)
    @show sum(sort(cal)[end-2:end])
end

main()
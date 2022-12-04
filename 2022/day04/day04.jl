function main()
    data = filter(x -> !isempty(x), split(readchomp("input.txt"), "\n"))

    mapreduce(+, data) do x
        m = parse.(Int, split(x, ('-', ',')))
        a, b = m[1]:m[2], m[3]:m[4]

        (a ⊆ b) | (b ⊆ a)  # part 1
        # !isdisjoint(a, b)  # part 2
    end
end

main()
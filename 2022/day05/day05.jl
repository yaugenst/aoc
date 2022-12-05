function main()
    stacks, moves = filter(x -> !isempty(x), split(readchomp("input.txt"), "\n\n"))

    stacks = split(stacks, "\n")
    idxs = only.(findall(r"\d+", stacks[end]))
    stack_ary = hcat(map(x -> getindex.(x, idxs), stacks[1:end-1])...)
    ds = Dict(k => filter(x -> x != ' ', v)
              for (k, v) in zip(1:length(idxs), eachrow(stack_ary)))

    for move in split(moves, "\n")
        a, b, c = map(x -> parse(Int, x.match), eachmatch(r"\d+", move))

        prepend!(ds[c], reverse(splice!(ds[b], 1:a)))  # part 1
        # prepend!(ds[c], splice!(ds[b], 1:a))  # part 2
    end

    @show join(map(x -> ds[x][1], 1:length(idxs)))
end

main()

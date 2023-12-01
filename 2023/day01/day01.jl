#!/usr/bin/env julia

function main()
    data = split(readchomp("input.txt"))

    x = map(data) do line
        m = collect(map(m -> m.match, eachmatch(r"\d", line)))
        parse(Int, m[begin] * m[end])
    end

    @show sum(x)

    mapper = Dict(
        "zero" => "0",
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9",
    )
    pattern = Regex(raw"\d|" * join(keys(mapper), "|"))

    x = map(data) do line
        matches = collect(map(m -> m.match, eachmatch(pattern, line, overlap = true)))
        m = map(x -> x in keys(mapper) ? mapper[x] : x, matches)
        parse(Int, m[begin] * m[end])
    end

    @show sum(x)
end

main()

Base.@kwdef struct RuleSet
    points::Dict{Char,Int} = Dict('X' => 1, 'Y' => 2, 'Z' => 3)
    win::Dict{Char,Char} = Dict('C' => 'X', 'A' => 'Y', 'B' => 'Z')
    draw::Dict{Char,Char} = Dict('A' => 'X', 'B' => 'Y', 'C' => 'Z')
    lose::Dict{Char,Char} = Dict('B' => 'X', 'C' => 'Y', 'A' => 'Z')
end

function get_score(a, b, r)
    score = r.points[b]
    if b == r.draw[a]
        score += 3
    elseif b == r.win[a]
        score += 6
    end
    return score
end

function main()
    data = filter(x -> !isempty(x), split(readchomp("input.txt"), "\n"))
    rules = RuleSet()

    part1 = mapreduce(x -> get_score(x[1], x[3], rules), +, data)
    @show part1

    d = Dict('X' => rules.lose, 'Y' => rules.draw, 'Z' => rules.win)
    part2 = mapreduce(x -> get_score(x[1], d[x[3]][x[1]], rules), +, data)
    @show part2
end

main()
function Base.:÷(x::Complex, y)
    real(x) ÷ y + 1im * (imag(x) ÷ y)
end

function main()
    data = split(strip(readchomp("input.txt")), "\n")
    len = 2  # 10 for part 2
    rope = fill(0 + 0im, len)
    moves = Dict{Char,ComplexF64}('L' => -1im, 'R' => 1im, 'U' => 1, 'D' => -1)
    hist = Set(rope)

    for line in data
        m, n = line[1], parse(Int, line[3:end])
        for _ in 1:n
            rope[1] += moves[m]
            for i in 2:len
                dist = rope[i-1] - rope[i]
                if abs(dist) >= 2
                    rope[i] = rope[i-1] - dist ÷ 2
                end
            end
            push!(hist, rope[end])
        end
    end
    length(hist)
end

main()

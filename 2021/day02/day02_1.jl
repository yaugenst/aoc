function main()
    data = read("input.txt", String)
    hpos = 0
    depth = 0

    for m in eachmatch(r"(\w+) (\d+)", data)
        cmd, val = m.captures[1], parse(Int32, m.captures[2])
        if cmd == "forward"
            hpos += val
        elseif cmd == "up"
            depth -= val
        elseif cmd == "down"
            depth += val
        end
    end

    println(depth * hpos)
end

main()
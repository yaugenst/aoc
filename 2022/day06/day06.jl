function find_unique_sequence(s, n, i=1)
    length(Set(s[i:i+n-1])) == n ? i + n - 1 : find_unique_sequence(s, n, i + 1)
end

function main()
    data = strip(readchomp("input.txt"))
    find_unique_sequence(data, 4)  # 14 for part 2
end

main()

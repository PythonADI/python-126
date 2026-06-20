x = "this is a good sentence"
counts = {}


for symbol in x:
    counts[symbol] = counts.get(symbol, 0) + 1
    # if symbol not in counts:
    #     counts[symbol] = 1
    # else:
    #     counts[symbol] += 1

print(counts)


def save(pairs):
    file = open("results.txt", "w")

    for giver in pairs:
        receiver = pairs[giver]
        file.write(giver + " -> " + receiver + '\n')

    file.close()

def animate(speed, init):
    length = len(init)
    chamber = list(init)
    states = []

    while any(c != '.' for c in chamber):
        states.append(''.join(['X' if c != '.' else '.' for c in chamber]))

        new_chamber = ['.'] * length
        for i, c in enumerate(chamber):
            if c == 'L' and i - speed >= 0:
                new_chamber[i - speed] = 'L'
            elif c == 'R' and i + speed < length:
                new_chamber[i + speed] = 'R'
        chamber = new_chamber
    states.append('.' * length)
    return states


print(animate(2, "..R...."))

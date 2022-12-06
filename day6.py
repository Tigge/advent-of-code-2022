def find_unique_range(data, length):
    for n in range(0, len(data) - length):
        if len(set(data[n : n + length])) == length:
            return n + length


def find_start_of_packet(data):
    return find_unique_range(data, 4)


def find_start_of_message(data):
    return find_unique_range(data, 14)


def parse(f):
    return f.read().strip()


with open("day6.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))

    print("Part 1:", find_start_of_packet(d))
    print("Part 2:", find_start_of_message(d))

def total_dir_size(dirs):
    return sum([folder[1] for folder in dirs.items() if folder[1] <= 100000])


def smallest_largest_dir_size(dirs):
    needed_disk_space = 30000000 - (70000000 - dirs["/"])
    return min([dir[1] for dir in dirs.items() if dir[1] >= needed_disk_space])


def parse(f):
    commands = [line.split() for line in f.readlines()]
    path = ["/"]
    dirs = dict()

    for command in commands:
        if command[0] == "$" and command[1] == "cd":
            if command[2] == "..":
                path.pop()
            elif command[2] == "/":
                path = ["/"]
            else:
                path.append(command[2])
        elif command[0] == "$" and command[1] == "ls":
            pass
        elif command[0] == "dir":
            pass
        else:
            for n in range(len(path)):
                wd = "/" + "/".join(path[1 : n + 1])
                dirs[wd] = dirs.get(wd, 0) + int(command[0])

    return dirs


with open("day7.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", total_dir_size(d))
    print("Part 2:", smallest_largest_dir_size(d))

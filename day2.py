SCORE1 = {
    "A X": 1 + 3,  # Rock - rock
    "A Y": 2 + 6,  # Rock - paper
    "A Z": 3 + 0,  # Rock - scissor
    "B X": 1 + 0,  # Paper - rock
    "B Y": 2 + 3,  # Paper - paper
    "B Z": 3 + 6,  # Paper - scissor
    "C X": 1 + 6,  # Scissor - rock
    "C Y": 2 + 0,  # Scissor - paper
    "C Z": 3 + 3,  # Scissor - scissor
}

SCORE2 = {
    "A X": 3 + 0,  # Rock - lose (scissor)
    "A Y": 1 + 3,  # Rock - draw (rock)
    "A Z": 2 + 6,  # Rock - win (scissor)
    "B X": 1 + 0,  # Paper - lose (rock)
    "B Y": 2 + 3,  # Paper - draw (paper)
    "B Z": 3 + 6,  # Paper - win (scissor)
    "C X": 2 + 0,  # Scissor - lose (paper)
    "C Y": 3 + 3,  # Scissor - draw (scissor)
    "C Z": 1 + 6,  # Scissor - win (scissor)
}


def find_score_1(moves):
    return sum(map(lambda score: SCORE1[score], moves))


def find_score_2(moves):
    return sum(map(lambda score: SCORE2[score], moves))


def parse(f):
    moves = map(lambda line: line.strip(), f.readlines())
    return list(moves)


with open("day2.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))
    print("Part 1:", find_score_1(d))
    print("Part 2:", find_score_2(d))

def read_data():
    with open("./data/new-wordle-answers-alphabetical.txt") as f:
        words = [line.strip() for line in f.readlines()]
    return words

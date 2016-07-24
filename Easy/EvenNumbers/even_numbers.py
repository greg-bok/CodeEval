import sys

def is_even(x):
    return x % 2 == 0

def process_line(lineText):
    if is_even(int(lineText)):
        return "1"
    else:
        return "0"

def process_lines(text):
    nonBlank = filter(lambda x: len(x.strip()) > 0, text.splitlines())
    return "\n".join(map(lambda x: process_line(x), nonBlank))

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as fd:
        print process_lines(fd.read())

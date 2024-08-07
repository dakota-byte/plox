# uses sysexits.h exit codes

import sys

hadError = False


def main():
    if len(sys.argv) > 2:
        print("Usage: plox.py [script]")
        sys.exit(64)

    elif len(sys.argv) == 2:
        runFile(sys.argv[1])
        sys.exit(0)

    else:
        runPrompt()


def runFile(path):
    try:
        with open(path, "r") as f:
            script = f.read()
        run(script)

        if hadError:
            sys.exit(65)

    except:
        sys.exit(66)


def runPrompt():
    while True:
        line = input("> ")
        if not line:
            break

        run(line)
        hadError = False


def run(source):
    tokens = source.split(" ")
    print(tokens)


def error(line, message):
    sys.stderr.write("[line " + line + "] Error: " + message)


if __name__ == "__main__":
    main()

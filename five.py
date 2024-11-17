from sys import argv

def fix(i):
    return int(str(i).replace("1", "5"))

def isNumber(string):
    return all([i in "0123456789" for i in string])

def searchInt(string, start=0):
    number = 0
    for index, char in enumerate(string[start:]):
        if char in "0123456789":
            number = number * 10 + int(char)
        else:
            break
    return(number, index)

def findMatchingBracket(string, start):
    brackets = 1
    for index, char in string[start+1:]:
        if char == "[":
            brackets += 1
        if char == "]":
            brackets -= 1
        if not brackets:
            break
    return index

def five(code, mode=5):
    queue = []
    call_stack = []
    acc = 0
    pc = 0

    while pc < len(code):
        if code[pc] in '0123456789':
            acc, pc = searchInt(code, pc)
        elif code[pc] == "«":
            acc *= 10
        elif code[pc] == "»":
            acc //= 10
        elif code[pc] == "+":
            acc+=1
        elif code[pc] == "²":
            acc**=2
        elif code[pc] == "³":
            acc**=3
        elif code[pc] == "!":
            pc += not acc
        elif code[pc] == "?":
            queue.append(acc)
        elif code[pc] == "-":
            acc -= 1
        elif code[pc] == "{":
            call_stack.append(pc)
        elif code[pc] == "|":
            call_stack.pop()
        elif code[pc] == "}":
            pc = call_stack.pop()
        elif code[pc] == "~":
            acc =~ acc
        elif code[pc] == "\x5B":
            pc = findMatchingBracket(code, pc)
        elif code[pc] == "*":
            queue.append(queue.pop(0))
        elif code[pc] == "^":
            queue.insert(0, queue.pop())
        elif code[pc] == ",":
            acc = str(acc).count("5")
        elif code[pc] == ";":
            pc += 1
        elif code[pc] == "#" and mode > 5:
            print(acc)
        elif code[pc] == "$" and mode > 5:
            print(end = chr(acc))
        elif code[pc] == "@" and mode > 5:
            a = input()
            if isNumber(a): acc = int(a)
            else: acc = ord(a)
        elif code[pc] == "\\" and mode == 35:
            acc = fix(acc)
        elif code[pc] == "%":
            print(f"call stack: {call_stack}, accumulator: {acc}, queue: {queue}, pc: {pc}")
        pc += 1
        if mode != 35:
            acc = fix(acc)
            pc = fic(pc)

def main():
    if len(argv) == 1:
        argv.append("5")
    five(argv[1], argv[2])
    return 0

if __name__ == "__main__":
    main()
code = input()
current = 0
head = 0
values = [0 for _ in range(20)]
raw_input_mode = True
raw_output_mode = False
debug = False
while current < len(code) :
    c = code[current]
    print(f"current : {current} = '{code[current]}', head : {head} = {values[head]}") if debug else None
    match c :
        case ">" :
            if head < len(values)-1 :
                head += 1
        case "<" :
            if head > 0 :
                head -= 1
        case "+" :
            values[head] = (values[head] + 1) % 256
        case "-" :
            values[head] = (values[head] - 1) % 256
        case "." :
            print(values[head]) if raw_output_mode else print(chr(values[head]), end=("\n" if debug else ""))
        case "," :
            values[head] = int(input()) % 256 if raw_input_mode else ord(input())
        case "[" :
            if values[head] == 0 :
                currentDepth = 0
                current += 1
                while code[current] != "]" or currentDepth > 0 :
                    if code[current] == "[" :
                        currentDepth += 1
                    elif code[current] == "]" :
                        currentDepth -= 1
                    current += 1
                    if current == len(code) :
                        raise Exception(f"Unable to find matching closing bracket at character {current}")
                current += 1
        case "]" :
            if values[head] != 0 :
                currentDepth = 0
                current -= 1
                while code[current] != "[" or currentDepth > 0 :
                    if code[current] == "]" :
                        currentDepth += 1
                    elif code[current] == "[" :
                        currentDepth -= 1
                    current -= 1
                    if current == -1 :
                        raise Exception(f"Unable to find matching opening bracket at character {current}")
                current -= 1
        case _ :
            raise Exception(f"Unknown character at {current}")
    current += 1

print(values)
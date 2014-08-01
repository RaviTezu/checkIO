#!/usr/bin/python

def digit_stack(commands):
    """Takes a sequence of commands:
       "PUSH X" -- add X in the stack, where X is a digit.
       "POP" -- look and remove the top position. If the stack is empty, then it returns 0 (zero) and does nothing.
       "PEEK" -- look at the top position. If the stack is empty, then it returns 0 (zero).
        The stack can only contain digits.
        Process all commands and sum all digits which were taken from the stack ("PEEK" or "POP"). 
       Initial value of the sum is 0 (zero). Returns sum """
    total_sum = 0 
    seq = []
    for command in commands:
        command_split = command.split(" ")
        #print "seq: ", seq, command_split[0]
        if command_split[0] == "PUSH":
            seq.append(int(command_split[1]))
        elif command_split[0] == "POP":
            try:
                total_sum = total_sum + seq[-1]
                seq = seq[:-1]
            except IndexError:
                pass
        elif command_split[0] == "PEEK":
            try:
                total_sum = total_sum + seq[-1]
            except IndexError:
                pass
        else:
            return 0
    return total_sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"

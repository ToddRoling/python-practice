# My solution to https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    command_count = int(input())
    list_ = []

    for command_index in range(command_count):
        command = input().split(' ')
        instruction = command[0]

        if len(command) == 1:
            if instruction == 'pop':
                list_.pop()
            elif instruction == 'print':
                print(list_)
            elif instruction == 'reverse':
                list_.reverse()
            elif instruction == 'sort':
                list_.sort()
        else:
            params = [int(n) for n in command[1:]]
            if instruction == 'append':
                list_.append(*params)
            elif instruction == 'insert':
                list_.insert(*params)
            elif instruction == 'remove':
                list_.remove(*params)

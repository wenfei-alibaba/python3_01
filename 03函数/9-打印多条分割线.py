def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    row = 0
    while row < 6:
        print_line(char, times)
        row += 1


print_lines("-", 20)

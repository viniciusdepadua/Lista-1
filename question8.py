def draw_table(size):
    """Prints a neat looking multiplication table
 with size size x size """

    tab = len(str(size * size))
    header = " " * tab + " " * (2 * tab) + "1"
    dash_counter = 2 * tab
    for i in range(2, size + 1):
        header += " " * (tab + 1 - len(str(i))) + str(i)
        dash_counter += tab + 1
    header += "\n"
    dash = " " * tab + ":" + "-" * dash_counter + "\n"
    body = ""
    for i in range(1, size + 1):
        body = body + " " * (tab - len(str(i))) + str(i) + ":"
        body = body + " " * (2 * tab - len(str(i * 1))) + str(i * 1)
        for j in range(2, size + 1):
            body = body + " " * (tab + 1 - len(str(j * i))) + str(j * i)
        body = body + "\n"
    print(header + dash + body)


def test_draw_table():
    draw_table(12)
    draw_table(20)
    draw_table(28)
    draw_table(36)


test_draw_table()
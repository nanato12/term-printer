from term_printer import Color256, cprint

# font color
for i in range(0, 256):
    cprint("{: ^4}".format(i), attrs=[Color256(i)], end="")
print()

# bg color
for i in range(0, 256):
    cprint(" " * 4, attrs=[Color256(i, is_bg=True)], end="")
print()

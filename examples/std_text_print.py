from term_printer import Color, Format, StdText, cprint

# default
cprint("this is a default pen")

# bold
cprint(f"this is a {StdText('bold', Format.BOLD)} pen")

# italic
cprint(f"this is a {StdText('italic', Format.ITALIC)} pen")

# reverse
cprint(f"this is a {StdText('reverse', Format.REVERSE)} pen")

# red color
cprint(f"this is a {StdText('red', Color.RED)} pen")

# background magenta color
cprint(f"this is a {StdText('bg magenta', Color.BG_MAGENTA)} pen")

# magenta color & italic
cprint(f"this is a {StdText('magenta', Color.MAGENTA)} {StdText('italic', Format.ITALIC)} pen")

# bold & italic
cprint(f"this is a {StdText('bold', Format.BOLD)} {StdText('italic', Format.ITALIC)} pen")

# cyan color & bold & italic
cprint(f"this is a {StdText('cyan', Color.CYAN)} {StdText('bold', Format.BOLD)} {StdText('italic', Format.ITALIC)} pen")

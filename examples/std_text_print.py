from term_printer import Color, Color256, ColorRGB, Format, StdText, cprint

# default
cprint("this is a default pen")

# bold
cprint(f"this is a {StdText('bold', Format.BOLD)} pen")

# italic
cprint(f"this is a {StdText('italic', Format.ITALIC)} pen")

# red color
cprint(f"this is a {StdText('red', Color.RED)} pen")

# bright red color
cprint(f"this is a {StdText('red', Color.BRIGHT_RED)} pen")

# background magenta color
cprint(f"this is a {StdText('bg magenta', Color.BG_MAGENTA)} pen")

# background bright magenta color
cprint(f"this is a {StdText('bg magenta', Color.BG_BRIGHT_MAGENTA)} pen")

# magenta color & italic
cprint(
    f"this is a {StdText('magenta', Color.MAGENTA)} {StdText('italic', Format.ITALIC)} pen"
)

# bold & italic
cprint(
    f"this is a {StdText('bold', Format.BOLD)} {StdText('italic', Format.ITALIC)} pen"
)

# cyan color & bold & italic
cprint(
    f"this is a {StdText('cyan', Color.CYAN)} {StdText('bold', Format.BOLD)} {StdText('italic', Format.ITALIC)} pen"
)


# 8-bit color 154
cprint(f"this is a {StdText('8-bit 154',Color256(154))} pen")

# 8-bit bg color 154 and magenta color
cprint(
    f"this is a {StdText('bg 8-bit 154', Color256(154, is_bg=True))} {StdText('magenta', Color.MAGENTA)} pen"
)

# rgb(100, 255, 255) color
cprint(f"this is a {StdText('rgb(100, 255, 255)', ColorRGB(100, 255, 255))} pen")

# bg rgb(100, 255, 255) color and black color
cprint(
    f"this is a {StdText('bg rgb(100, 255, 255)', ColorRGB(100, 255, 255, is_bg=True))} {StdText('black', Color.BLACK)} pen",
)

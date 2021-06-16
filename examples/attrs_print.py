from term_printer import Color, Color256, ColorRGB, Format, cprint

# default
cprint("this is a default pen")

# bold
cprint("this is a bold pen", attrs=[Format.BOLD])

# italic
cprint("this is a italic pen", attrs=[Format.ITALIC])

# red color
cprint("this is a red pen", attrs=[Color.RED])

# bright red color
cprint("this is a bright red pen", attrs=[Color.BRIGHT_RED])

# background magenta color
cprint("this is a bg magenta pen", attrs=[Color.BG_MAGENTA])

# background bright magenta color
cprint("this is a bg bright magenta pen", attrs=[Color.BG_BRIGHT_MAGENTA])

# magenta color & italic
cprint("this is a magenta italic pen", attrs=[Color.MAGENTA, Format.ITALIC])

# bold & italic
cprint("this is a bold italic pen", attrs=[Format.BOLD, Format.ITALIC])

# cyan color & bold & italic
cprint("this is a cyan bold italic pen", attrs=[Color.CYAN, Format.BOLD, Format.ITALIC])

# 8-bit color 154
cprint("this is a 8-bit 154 pen", attrs=[Color256(154)])

# 8-bit bg color 154 and magenta color
cprint("this is a bg 8-bit 154 pen", attrs=[Color256(154, is_bg=True), Color.MAGENTA])

# rgb(100, 255, 255) color
cprint("this is a rgb(100, 255, 255) pen", attrs=[ColorRGB(100, 255, 255)])

# bg rgb(100, 255, 255) color and black color
cprint(
    "this is a bg rgb(100, 255, 255) pen",
    attrs=[ColorRGB(100, 255, 255, is_bg=True), Color.BLACK],
)

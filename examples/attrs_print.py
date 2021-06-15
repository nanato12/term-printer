from term_printer import Color, Format, cprint

# default
cprint("this is a default pen")

# bold
cprint("this is a bold pen", attrs=[Format.BOLD])

# italic
cprint("this is a italic pen", attrs=[Format.ITALIC])

# reverse
cprint("this is a reverse pen", attrs=[Format.REVERSE])

# red color
cprint("this is a red pen", attrs=[Color.RED])

# background magenta color
cprint("this is a bg magenta pen", attrs=[Color.BG_MAGENTA])

# magenta color & italic
cprint("this is a magenta italic pen", attrs=[Color.MAGENTA, Format.ITALIC])

# bold & italic
cprint("this is a bold italic pen", attrs=[Format.BOLD, Format.ITALIC])

# cyan color & bold & italic
cprint("this is a cyan bold italic pen", attrs=[Color.CYAN, Format.BOLD, Format.ITALIC])

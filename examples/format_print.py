from term_printer import Format, StdText, cprint

cprint(StdText("1234567890", Format.BOLD))
cprint(StdText("1234567890", Format.FAINT))
cprint(StdText("1234567890", Format.ITALIC))
cprint(StdText("1234567890", Format.UNDERLINE))
cprint(StdText("1234567890", Format.BLINK))
cprint(StdText("1234567890", Format.FAST_BLINK))
cprint(StdText("1234567890", Format.REVERSE))
cprint(StdText("1234567890", Format.CONCEAL))
cprint(StdText("1234567890", Format.STRIKE))

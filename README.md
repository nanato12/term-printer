# term-printer
Print 'text color' and 'text format' on Term with Python

**※ It may not work depending on the OS and shell used.**

## Usage

### 1. Color print

#### **[source](./examples/color_print.py)**

```python
from term_printer import Color, StdText, cprint

cprint(StdText("1234567890", Color.BLACK))
cprint(StdText("1234567890", Color.RED))
cprint(StdText("1234567890", Color.GREEN))
cprint(StdText("1234567890", Color.YELLOW))
cprint(StdText("1234567890", Color.BLUE))
cprint(StdText("1234567890", Color.MAGENTA))
cprint(StdText("1234567890", Color.CYAN))
cprint(StdText("1234567890", Color.WHITE))
cprint(StdText("1234567890", Color.DEFAULT))
```

#### result

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/examples_color_print_result.png">

### 2. Background color print

#### **[source](./examples/bg_color_print.py)**

```python
from term_printer import Color, StdText, cprint

cprint(StdText("1234567890", Color.BG_BLACK))
cprint(StdText("1234567890", Color.BG_RED))
cprint(StdText("1234567890", Color.BG_GREEN))
cprint(StdText("1234567890", Color.BG_YELLOW))
cprint(StdText("1234567890", Color.BG_BLUE))
cprint(StdText("1234567890", Color.BG_MAGENTA))
cprint(StdText("1234567890", Color.BG_CYAN))
cprint(StdText("1234567890", Color.BG_WHITE))
cprint(StdText("1234567890", Color.BG_DEFAULT))
```

#### result

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/examples_bg_color_print_result.png">

### 3. Format print

#### **[source](./examples/format_print.py)**

```python
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
```

#### result

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/examples_format_print_result.png">

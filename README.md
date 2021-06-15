# term-printer
Print 'text color' and 'text format' on Term with Python

**※ It may not work depending on the OS and shell used.**

## PIP

```bash
$ pip install term-printer
```

## import

```python
from term_printer import Color, StdText, cprint
```

If you want to override bultin `print` function


```python
from term_printer import Color, StdText, cprint as print
```


## Usage

### 1. Attrs print

Applies to all characters.

#### **[source](https://github.com/nanato12/term-printer/blob/main/examples/attrs_print.py)**

```python
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
```

#### result

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/examples_attrs_print_result.png">

### 1. Color print

#### **[source](https://github.com/nanato12/term-printer/blob/main/examples/color_print.py)**

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

#### **[source](https://github.com/nanato12/term-printer/blob/main/examples/bg_color_print.py)**

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

#### **[source](https://github.com/nanato12/term-printer/blob/main/examples/format_print.py)**

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

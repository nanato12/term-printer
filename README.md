# term-printer
Print 'text color' and 'text format' on Term with Python

**※ It may not work depending on the OS and shell used.**

## PIP

```bash
$ pip install term-printer
```

## import

```python
from term_printer import Color, Color256, ColorRGB, StdText, cprint
```

If you want to override bultin `print` function


```python
from term_printer import Color, Color256, ColorRGB, StdText, cprint as print
```


## Usage

### 1. Attrs print

Applies to all characters.

You can specify `Format`, `Color`, `Color256`, and `ColorRGB`.

Able to specify more than one.

#### **[source](https://github.com/nanato12/term-printer/blob/main/examples/attrs_print.py)**

```python
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
```

#### result

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/examples_attrs_print_result.png">

### 2. StdText print

#### **[source](https://github.com/nanato12/term-printer/blob/main/examples/std_text_print.py)**

```python
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
```

#### result

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/examples_std_text_print_result.png">


## Color

```python
class Color(Enum)
```

Enum class.

Example
```python
from term_printer import Color

Color.RED  # RED foreground color
Color.BG_RED  # RED background color

Color.BLUE  # BLUE foreground color
Color.BG_BLUE  # BLUE background color
```

### **[source](https://github.com/nanato12/term-printer/blob/main/examples/std_text_print.py#L20-L52)**

Definition is [3-bit and 4-bit colors](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit)

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/color.png">


## Color256

```python
class Color256(n: int, is_bg: bool = False)
```

- First argument takes `int` (0 - 255).

- Second argument takes `bool` (default: False).
False: change foreground color
True: change background color

Example
```python
from term_printer import Color256

Color256(9)  # RED foreground color
Color256(9, True)  # RED background color

Color256(12)  # BLUE foreground color
Color256(12, True)  # BLUE background color
```

Definition is [8-bit 256 colors](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit)

<img src="https://raw.githubusercontent.com/nanato12/term-printer/main/docs/images/color256.png">

## ColorRGB

```python
class ColorRGB(r: int, g: int, b: int, is_bg: bool = False)
```

- Three arguments takes `int` (0 - 255).

- Fourth argument takes `bool` (default: False).
False: change foreground color
True: change background color

Example
```python
from term_printer import ColorRGB

ColorRGB(255, 0, 0)  # RED foreground color
ColorRGB(255, 0, 0, True)  # RED background color

ColorRGB(0, 0, 255)  # BLUE foreground color
ColorRGB(0, 0, 255, True)  # BLUE background color
```

## Format

```python
class Format(Enum):
    BOLD = 1
    FAINT = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5
    FAST_BLINK = 6
    REVERSE = 7
    CONCEAL = 8
    STRIKE = 9
```

Enum class.

Example
```python
from term_printer import Format

Format.BOLD  # BOLD font
Format.FAINT  # FAINT font
Format.ITALIC  # ITALIC font
Format.UNDERLINE  # UNDERLINE font
```

Definition is [SGR](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters)

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

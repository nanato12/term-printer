"""
Copyright 2021 nanato12

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from enum import IntEnum, IntFlag, auto


class WinColor(IntFlag):
    BLACK = 0
    BLUE = 1
    GREEN = 2
    CYAN = 3
    RED = 4
    MAGENTA = 5
    YELLOW = 6
    WHITE = 7
    BRIGHT_BLACK = BLACK | 0x08
    BRIGHT_BLUE = BLUE | 0x08
    BRIGHT_GREEN = GREEN | 0x08
    BRIGHT_CYAN = CYAN | 0x08
    BRIGHT_RED = RED | 0x08
    BRIGHT_MAGENTA = MAGENTA | 0x08
    BRIGHT_YELLOW = YELLOW | 0x08
    BRIGHT_WHITE = WHITE | 0x08
    BG_BLACK = BLACK << 4
    BG_BLUE = BLUE << 4
    BG_GREEN = GREEN << 4
    BG_CYAN = CYAN << 4
    BG_RED = RED << 4
    BG_MAGENTA = MAGENTA << 4
    BG_YELLOW = YELLOW << 4
    BG_WHITE = WHITE << 4
    BG_BRIGHT_BLACK = BRIGHT_BLACK << 4
    BG_BRIGHT_BLUE = BRIGHT_BLUE << 4
    BG_BRIGHT_GREEN = BRIGHT_GREEN << 4
    BG_BRIGHT_CYAN = BRIGHT_CYAN << 4
    BG_BRIGHT_RED = BRIGHT_RED << 4
    BG_BRIGHT_MAGENTA = BRIGHT_MAGENTA << 4
    BG_BRIGHT_YELLOW = BRIGHT_YELLOW << 4
    BG_BRIGHT_WHITE = BRIGHT_WHITE << 4


class Color(IntEnum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    BRIGHT_BLACK = 90
    BRIGHT_RED = 91
    BRIGHT_GREEN = 92
    BRIGHT_YELLOW = 93
    BRIGHT_BLUE = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN = 96
    BRIGHT_WHITE = 97
    BG_BLACK = 40
    BG_RED = 41
    BG_GREEN = 42
    BG_YELLOW = 43
    BG_BLUE = 44
    BG_MAGENTA = 45
    BG_CYAN = 46
    BG_WHITE = 47
    BG_BRIGHT_BLACK = 100
    BG_BRIGHT_RED = 101
    BG_BRIGHT_GREEN = 102
    BG_BRIGHT_YELLOW = 103
    BG_BRIGHT_BLUE = 104
    BG_BRIGHT_MAGENTA = 105
    BG_BRIGHT_CYAN = 106
    BG_BRIGHT_WHITE = 107

    @property
    def win32_value(self):
        return WinColor[self.name]


class Color256:
    __n: int
    is_bg: bool

    def __init__(self, n: int, is_bg: bool = False) -> None:
        if not (0 <= n <= 255):
            raise Exception(f"Invalid 256bit color number: {n}")
        self.__n = n
        self.is_bg = is_bg

    def __str__(self) -> str:
        tag: str = "48" if self.is_bg else "38"
        return f"{tag};5;{self.__n}"


class ColorRGB:
    __r: int
    __g: int
    __b: int
    is_bg: bool

    def __init__(self, r: int, g: int, b: int, is_bg: bool = False) -> None:
        for k, n in {"R": r, "G": g, "B": b}.items():
            if not (0 <= n <= 255):
                raise Exception(f"Invalid 256bit color number: {k}:{n}")
        self.__r = r
        self.__g = g
        self.__b = b
        self.is_bg = is_bg

    def __str__(self) -> str:
        tag: str = "48" if self.is_bg else "38"
        return f"{tag};2;{self.__r};{self.__g};{self.__b}"

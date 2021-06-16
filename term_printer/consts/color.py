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

from enum import Enum


class Color(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39
    LIGHT_GRAY = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96
    LIGHT_WHITE = 97
    BG_BLACK = 40
    BG_RED = 41
    BG_GREEN = 42
    BG_YELLOW = 43
    BG_BLUE = 44
    BG_MAGENTA = 45
    BG_CYAN = 46
    BG_WHITE = 47
    BG_DEFAULT = 49


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
    __R: int
    __G: int
    __B: int
    is_bg: bool

    def __init__(self, R: int, G: int, B: int, is_bg: bool = False) -> None:
        for k, n in {"R": R, "G": G, "B": B}.items():
            if not (0 <= n <= 255):
                raise Exception(f"Invalid 256bit color number: {k}:{n}")
        self.__R = R
        self.__G = G
        self.__B = B
        self.is_bg = is_bg

    def __str__(self) -> str:
        tag: str = "48" if self.is_bg else "38"
        return f"{tag};2;{self.__R};{self.__G};{self.__B}"

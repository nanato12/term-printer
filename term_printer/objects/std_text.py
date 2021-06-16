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

from typing import Optional, Union

from ..consts.color import Color, Color256, ColorRGB
from ..consts.format import Format


class StdText:
    __text: str
    option: Optional[Union[Color, Color256, ColorRGB, Format, int]]

    def __init__(
        self,
        text: str,
        option: Optional[Union[Color, Color256, ColorRGB, Format, int]] = None,
    ) -> None:
        self.__text = text
        self.option = option

    def __str__(self) -> str:
        if self.option is None:
            return self.__text
        elif isinstance(self.option, (Color, Format)):
            value = self.option.value
        else:
            value = self.option
        return f"\033[{value}m{self.__text}\033[m"

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

from typing import List, Union

from .consts.color import Color, Color256, ColorRGB
from .consts.format import Format
from .objects.std_text import StdText

__description__ = "Print 'text color' and 'text format' on Term with Python"
__copyright__ = "Copyright 2021 nanato12"
__version__ = "1.1"
__license__ = "Apache License 2.0"
__author__ = "nanato12"
__author_email__ = "admin@nanato12.info"
__url__ = "https://github.com/nanato12/term-printer"


def cprint(
    *args, attrs: List[Union[Color, Color256, ColorRGB, Format, int]] = [], **kwargs
) -> None:  # type:ignore

    if not isinstance(attrs, list):
        raise Exception("'attrs' should be list or None")

    stdout = []
    for arg in args:
        for attr in attrs:
            if not isinstance(attr, (Color, Color256, ColorRGB, Format, int)):
                raise Exception(
                    "'attrs' must be a list of Color, Color256, ColorRGB, Format, int"
                )
            arg = StdText(str(arg), attr)
        stdout.append(arg)

    print(*stdout, **kwargs)

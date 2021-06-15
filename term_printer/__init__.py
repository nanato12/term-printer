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

from .consts.color import Color
from .consts.format import Format
from .objects.std_text import StdText

__description__ = "Print 'text color' and 'text format' on Term with Python"
__copyright__ = "Copyright 2021 nanato12"
__version__ = "1.0.0"
__license__ = "Apache-2.0"
__author__ = "nanato12"
__author_email__ = "admin@nanato12.info"
__url__ = "https://github.com/nanato12/term-printer"


def cprint(*args, **kwargs) -> None:  # type:ignore
    stdout = []
    for arg in args:
        if isinstance(arg, StdText):
            arg = str(arg)
        stdout.append(arg)

    print(*stdout, **kwargs)

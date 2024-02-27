import fnmatch
import os

from functools import partial
from typing import Callable, List, Union


def list_files(
    path: str,
    filename_filter: Union[str, Callable[[str], bool]] = "*",
    recursive: bool = True,
    absolute: bool = False,
) -> List[str]:
    """List all filenames at a given path."""

    # - Get filenames

    if not recursive:
        filenames = os.listdir(path)
        filenames = [filename for filename in filenames if os.path.isfile(filename)]
    else:
        if os.path.isfile(path):
            filenames = [path]
        else:
            # glob.glob('**/*') is slower 2.5 times than simple os.walk. It also returns directories
            filenames = []
            for root, dirs, files in os.walk(path):
                filenames += [os.path.join(root, filename) for filename in files]

    # - Make filter callable if it's a string

    if isinstance(filename_filter, str):
        filename_filter = partial(fnmatch.fnmatch, pat=filename_filter)

    # - Filter

    filenames = [filename for filename in filenames if filename_filter(filename)]

    # - Make absolute if needed

    if absolute:
        filenames = [os.path.abspath(filename) for filename in filenames]

    # - Return

    return filenames


def test():
    print(list_files("."))
    print(list_files(".", absolute=True))


if __name__ == "__main__":
    test()

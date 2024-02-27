import sys

from stepwise_code.format_file import format_file
from stepwise_code.list_files import list_files


def main(*sources):
    assert len(sources) > 0, "Specify sources"
    for source in sources:
        for filename in list_files(source):
            format_file(filename)


if __name__ == "__main__":
    main(*sys.argv[1:])

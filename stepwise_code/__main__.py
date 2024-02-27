import fire

from deeplay.utils.list_files import list_files
from deeplay.utils.loguru_utils import configure_loguru
from deeplay.utils.wise_comments.format_file import format_file


def main(*sources):
    assert len(sources) > 0, "Specify sources"
    for source in sources:
        for filename in list_files(source):
            format_file(filename)


if __name__ == "__main__":
    configure_loguru()
    fire.Fire(main)

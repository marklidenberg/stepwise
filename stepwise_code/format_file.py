import os

from stepwise_code.file_extension_to_single_line_comment import file_extension_to_single_line_comment
from stepwise_code.format_code.format_code import format_code


def format_file(filename: str):
    """Read, format and write file."""

    # - Read file

    if not os.path.exists(filename):
        raise Exception(f"File not found: {filename}")

    with open(filename, encoding="utf-8") as f:
        text = f.read()

    # - Get file extension

    file_extension = os.path.splitext(filename)[-1]

    if file_extension not in file_extension_to_single_line_comment:
        raise Exception(f"File extension not supported: {file_extension}")

    # - Format code

    text = format_code(
        text,
        single_line_comment=file_extension_to_single_line_comment[file_extension],
    )

    # - Write file

    with open(filename + ".tmp", "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(filename + ".tmp", filename)


# see `format_code.py` for formatter test

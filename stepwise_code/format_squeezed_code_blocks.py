import re
import textwrap

from sortedcontainers import SortedList

from stepwise_code.clean_test_string import clean_test_string


def format_squeezed_code_blocks(text: str, line_comment_symbol: str = "#") -> str:
    def is_empty_or_comment_line(text):
        if "\n" in text:
            return False

        return re.sub(r"\s", "", text)[:1] in ["", "#"]

    # - Split lines

    lines = text.split("\n")

    # - Collect line infos

    line_infos = []
    current_start = 0
    for line in lines:
        line_info = {}
        line_info["line"] = line
        line_info["start"] = current_start
        line_info["end"] = current_start + len(line) + 1
        current_start += len(line) + 1
        line_infos.append(line_info)

    line_infos = SortedList(line_infos, key=lambda value: value["start"])

    # - Calculate indexes of lines that need new line inserted

    new_line_indexes = []

    for match in re.finditer(rf"^([ ]*){re.escape(line_comment_symbol)}([^\n]+)", text, flags=re.MULTILINE | re.DOTALL):
        # - Find line before

        comment_start = match.span()[0]
        comment_finish = match.span()[1]
        line_before_info_index = line_infos.bisect_left({"start": comment_start}) - 1

        if line_before_info_index == -1:
            line_before = None
        else:
            line_before = line_infos[line_before_info_index]["line"]

        # - Skip case when previous symbol is not "\"

        if line_before and line_before[-1] == "\\":
            continue

        # - Find line after

        line_after_info_index = line_infos.bisect_right({"start": comment_finish})

        if line_after_info_index == len(line_infos):
            line_after = None
        else:
            line_after = line_infos[line_after_info_index]["line"]
        if line_before and line_after:
            # Lines before and after present

            if not is_empty_or_comment_line(line_before) and not is_empty_or_comment_line(line_after):
                # fmt: off
                """
                Squeezed comment example

                some code here
                # squeezed pre-comment example
                some code here
                """
                # fmt: on
                new_line_indexes.append(line_before_info_index)

    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(line)
        if i in new_line_indexes:
            new_lines.append("")

    return "\n".join(new_lines)


# fmt: off

def test():
    text1 = """
    # a
    a = 1
    # b
    b = 2
    """

    text2 = """
    # a
    a = 1

    # b
    b = 2
    """

    assert clean_test_string(format_squeezed_code_blocks(text1)) == clean_test_string(text2)

# fmt: on

if __name__ == "__main__":
    test()

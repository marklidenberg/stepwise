import re

from stepwise_code.format_code.clean_test_string import clean_test_string


def prefix_non_formatted_lines(text: str, single_line_comment: str = "#") -> str:
    """Add special prefixes to lines that should not be formatted 'STEPWISE_CODE_OFF: '"""

    # - Iterate over lines

    formatting_enabled = True
    new_lines = []

    for line in text.split("\n"):
        # - Prepare patterns

        spaces_pattern = r"(?:[ ]*)"
        single_comment_prefix_pattern = rf"{spaces_pattern}{re.escape(single_line_comment)}{spaces_pattern}"

        # - Process `fmt: off`

        if re.search(pattern=rf"^{single_comment_prefix_pattern}fmt:{spaces_pattern}off", string=line):
            formatting_enabled = False

        # - Process `fmt: skip` and add prefix `STEPWISE_CODE_OFF: ` if formatting is disabled

        if not formatting_enabled or re.search(
            pattern=rf"{single_comment_prefix_pattern}fmt:{spaces_pattern}skip", string=line
        ):
            new_lines.append("STEPWISE_CODE_OFF: " + line)
        else:
            new_lines.append(line)

        # - Process `fmt: on`

        if re.search(pattern=rf"^{single_comment_prefix_pattern}fmt:{spaces_pattern}on", string=line):
            formatting_enabled = True
    return "\n".join(new_lines)


def unprefix_non_formatted_lines(text: str) -> str:
    """Remove 'STEPWISE_CODE_OFF: ' prefixes"""

    return re.sub(
        pattern="^STEPWISE_CODE_OFF: ",
        repl="",
        string=text,
        flags=re.MULTILINE,
    )


def test():
    text1 = """
    
    # fmt: off
    
    a = 1
    
    # fmt: on
    
    b = 2
    c = 3 # fmt: skip
    
    """

    text2 = """
            
    STEPWISE_CODE_OFF:     # fmt: off
    STEPWISE_CODE_OFF:     
    STEPWISE_CODE_OFF:     a = 1
    STEPWISE_CODE_OFF:     
    STEPWISE_CODE_OFF:     # fmt: on
        
        b = 2
    STEPWISE_CODE_OFF:     c = 3 # fmt: skip
    """

    assert clean_test_string(prefix_non_formatted_lines(text1)) == clean_test_string(text2)
    assert clean_test_string(unprefix_non_formatted_lines(clean_test_string(text2))) == clean_test_string(text1)
    assert clean_test_string(unprefix_non_formatted_lines(prefix_non_formatted_lines(text1))) == clean_test_string(
        text1
    )


if __name__ == "__main__":
    test()

import re
import textwrap

from stepwise_code.clean_test_string import clean_test_string


def mark_non_formatted_lines(text: str, line_comment: str = "#") -> str:
    """Prefix non-formatted lines with 'WISE_FORMATTING_OFF: '"""

    is_formatting_on = True
    new_lines = []
    for line in text.split("\n"):
        spaces = r"(?:[ ]*)"
        single_comment_prefix = rf"{spaces}{re.escape(line_comment)}{spaces}"
        if re.search(pattern=rf"^{single_comment_prefix}fmt:{spaces}off", string=line):
            is_formatting_on = False

        if re.search(pattern=rf"{single_comment_prefix}fmt:{spaces}skip", string=line) or not is_formatting_on:
            new_lines.append("STEPWISE_CODE_OFF: " + line)
        else:
            new_lines.append(line)

        if re.search(pattern=rf"^{single_comment_prefix}fmt:{spaces}on", string=line):
            is_formatting_on = True
    return "\n".join(new_lines)


def unmark_non_formatted_lines(text: str) -> str:
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

    assert clean_test_string(mark_non_formatted_lines(text1)) == clean_test_string(text2)
    assert clean_test_string(unmark_non_formatted_lines(text2)) == clean_test_string(text1)


if __name__ == "__main__":
    test()

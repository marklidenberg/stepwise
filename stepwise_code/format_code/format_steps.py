import re

from stepwise_code.format_code.clean_test_string import clean_test_string
from stepwise_code.format_code.repeat_symbol_split import repeat_symbol_split


def format_steps(text: str, line_comment_symbol: str = "#") -> str:
    """Format code steps.

    - Make first letter of step title upper case: `- step 1` -> `- Step 1`.
    - Remove trailing dots from step title: `- Step 1...` -> `- Step 1`.
    - Remove extra spaces around `-`: # -    step 1.` -> `# - step 1`
    - Leave exactly one empty line before and after each step.

    """

    # - Prepare re.sub arguments

    def _substitutor(match: re.Match, text: str) -> str:
        (
            spaces1,
            dashes,
            spaces2,
            text,
        ) = match.groups()  # sample comment: (spaces1) # (spaces2) (dashes, like ----) (spaces3) (text)
        text = text.strip()
        text = text[0].upper() + text[1:]
        text = re.sub(r"[\.]*$", "", text)
        return f"\n{spaces1}{line_comment_symbol} {repeat_symbol_split('-', len(dashes))} {text.strip()}\n\n"

    empty_line_pattern = rf"(?:[ ]*\n)"
    pattern = rf"^{empty_line_pattern}*([ ]*){re.escape(line_comment_symbol)} (-+)([ ]+)([^\n]+){empty_line_pattern}*"

    # - Run re.sub

    return re.sub(
        pattern=pattern,
        repl=lambda match: _substitutor(match, text=text),
        string=text,
        flags=re.MULTILINE,
    )


# fmt: off

def test():
    text1 = """
    # -    step 1.
    a = 1
    # -- sub-step 1.
    b = 2
    # -- sub-step 2...
    c = 3
    """

    text2 = """
    # - Step 1

    a = 1

    # -- Sub-step 1

    b = 2

    # -- Sub-step 2

    c = 3
    """

    assert clean_test_string(format_steps(text1)) == clean_test_string(text2)

# fmt: on

if __name__ == "__main__":
    test()

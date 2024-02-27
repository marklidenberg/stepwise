from stepwise_code.format_code.clean_test_string import clean_test_string
from stepwise_code.format_code.format_steps import format_steps
from stepwise_code.format_code.wrap_non_formatted_lines import mark_non_formatted_lines, unmark_non_formatted_lines


def format_code(text: str, single_line_comment: str = "#") -> str:
    """Apply stepwise-code formatter."""

    # - Mark unformatted code

    text = mark_non_formatted_lines(text)  # add special prefixes to lines that should not be formatted

    # - Format steps

    text = format_steps(text, line_comment_symbol=single_line_comment)

    # - Unmark non formatted lines

    text = unmark_non_formatted_lines(text)  # remove special prefixes from lines that should not be formatted

    # - Return

    return text


# fmt: off

def test():
    text1 = """
    # -    step 1.
    a = 1
    # -- sub-step 1.
    b = 2
    # -- sub-step 2...
    c = 3
    
    # fmt: off
    # -    step 1.
    a = 1
    # fmt: on
    
    # -    step 1. # fmt: skip 
    """

    text2 = """

    # - Step 1

    a = 1

    # -- Sub-step 1

    b = 2

    # -- Sub-step 2

    c = 3
    
    # fmt: off
    # -    step 1.
    a = 1
    # fmt: on
    
    # -    step 1. # fmt: skip 
    """

    assert clean_test_string(format_code(text1)) == clean_test_string(text2)

# fmt: on

if __name__ == "__main__":
    test()

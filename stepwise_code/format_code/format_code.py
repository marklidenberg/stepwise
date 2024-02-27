from stepwise_code.format_code.clean_test_string import clean_test_string
from stepwise_code.format_code.format_steps import format_steps
from stepwise_code.format_code.prefix_non_formatted_lines import (
    prefix_non_formatted_lines,
    unprefix_non_formatted_lines,
)


def format_code(text: str, single_line_comment: str = "#") -> str:
    """Apply stepwise-code formatter."""
    text = prefix_non_formatted_lines(text)
    text = format_steps(text, line_comment_symbol=single_line_comment)
    text = unprefix_non_formatted_lines(text)
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
    # --- sub-sub-step
    d = 4
    # ---- sub-sub-sub step
    
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
    
    # --- Sub-sub-step

    d = 4
    
    # --- - Sub-sub--sub step
    
    # fmt: off
    # -    step 1.
    a = 1
    # fmt: on
    
    # -    step 1. # fmt: skip 
    """

    print(clean_test_string(format_code(text1)))

# fmt: on

if __name__ == "__main__":
    test()

from stepwise_code.format_code.format_squeezed_code_blocks import format_squeezed_code_blocks
from stepwise_code.format_code.format_steps import format_steps
from stepwise_code.format_code.wrap_non_formatted_lines import mark_non_formatted_lines, unmark_non_formatted_lines


def format_code(text: str, single_line_comment: str = "#") -> str:
    """Apply stepwise-code formatter."""

    # - Mark unformatted code

    text = mark_non_formatted_lines(text)  # add special prefixes to lines that should not be formatted

    # - Format

    text = format_steps(text, line_comment_symbol=single_line_comment)
    text = format_squeezed_code_blocks(text, single_line_comment=single_line_comment)

    # - Unmark non formatted lines

    text = unmark_non_formatted_lines(text)  # remove special prefixes from lines that should not be formatted

    # - Return

    return text

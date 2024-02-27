import textwrap


def clean_test_string(s: str) -> str:
    return textwrap.dedent(s).strip()

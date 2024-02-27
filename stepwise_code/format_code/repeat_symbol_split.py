def repeat_symbol_split(symbol: str, count: int, split_number: int = 3) -> str:
    """
    assert repeat_symbol_split(symbol="-", count=10, split_number=3) == "--- --- --- -"
    """

    return " ".join([symbol * split_number] * (count // split_number) + [symbol * (count % split_number)])


def test():
    assert repeat_symbol_split(symbol="-", count=10, split_number=3) == "--- --- --- -"


if __name__ == "__main__":
    test()

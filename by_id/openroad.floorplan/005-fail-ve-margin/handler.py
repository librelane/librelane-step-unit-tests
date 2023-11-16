import re


def handle(step, exception, caplog):
    assert exception is not None, "Didn't fail on negative core margin"
    # [ERROR STA-0414] -core_space '-4.6000000000000005' is not a positive float
    error_match = [
        match
        for match in caplog.text.split("\n")
        if re.match(
            r"\[ERROR STA-0414\] -core_space .*is not a positive float.*", match
        )
    ]
    assert error_match != [], "Error STA-0414 not found"

import re


def handle(step, exception, caplog):
    assert (
        exception is not None
    ), "Fill insertion didn't fail on bad fill cell defintion"
    errors = [
        line
        for line in caplog.text.split("\n")
        if re.match(r"\[ERROR DPL-0002\] could not fill gap of size.*", line)
    ]
    assert errors, "ERROR DPL-0002 could not fill gap of size .. is not found"

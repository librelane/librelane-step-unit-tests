import re


def handle(step, exception, caplog):
    assert exception is not None, "Detalied router didn't raise an exception"
    # [ERROR DRT-0155] Guide in net _000_ uses layer met1 (4) that is outside the allowed routing range
    found = False
    for line in caplog.text.split("\n"):
        if re.match(
            r".*\[ERROR DRT-0155\].*that is outside the allowed routing range.*", line
        ):
            found = True
    assert found, "Error message DRT-0155 not found"

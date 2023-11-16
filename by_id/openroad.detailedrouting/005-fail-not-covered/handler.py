import re


def handle(step, exception, caplog):
    assert exception is not None, "Detalied router didn't raise an exception"
    # [ERROR DRT-0218] Guide is not connected to design
    found = False
    for line in caplog.text.split("\n"):
        if re.match(r".*\[ERROR DRT-0218\].*Guide is not connected.*", line):
            found = True
    assert found, "Error message DRT-0218 not found"

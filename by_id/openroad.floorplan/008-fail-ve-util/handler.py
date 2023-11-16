import re


def handle(step, exception, caplog):
    assert exception is not None, "Didn't fail on negative utilization"
    error = r"\[ERROR IFP-0012\].*"
    error_match = [match for match in caplog.text.split("\n") if re.match(error, match)]
    assert error_match != [], f"{error} not found"

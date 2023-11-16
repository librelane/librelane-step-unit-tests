import re


def handle(step, exception, caplog):
    assert exception is not None, "Didn't fail on non routed design"
    error = r"\[ERROR ANT-0008\] No detailed or global routing found.*"
    matches = [match for match in caplog.text.split("\n") if re.match(error, match)]

    assert matches != [], f"Did not find '{error}' in the log"

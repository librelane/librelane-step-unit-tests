import re


def handle(step, exception, caplog):
    assert exception is not None, "Check nodes didn't catch missing PDN"
    error_regex = r".*Unable to find \S+ layer.*"
    matches = [line for line in caplog.text.split("\n") if re.match(error_regex, line)]
    assert matches != [], f"Didn't find {error_regex} in log"

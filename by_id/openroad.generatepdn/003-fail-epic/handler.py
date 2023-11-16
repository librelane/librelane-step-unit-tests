def handle(step, exception, caplog):
    assert exception is not None, "Check nodes didn't catch missing PDN"
    error_msg = "Check connectivity failed"
    assert error_msg in caplog.text, f"{error_msg} not found in log"

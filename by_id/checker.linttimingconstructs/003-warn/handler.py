def handle(step, caplog):
    warning_msg = "The Lint Timing Errors metric was not found"
    assert (
        warning_msg in caplog.text
    ), f"Warning message: '{warning_msg}' not reported\n.Perhaps the error message changed?"

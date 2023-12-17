def handle(step, exception, caplog):
    assert exception is not None, "An extra pin did not raise an exception"
    assert (
        "not found in config but found in design" in caplog.text
    ), "no message printed about extra pin"

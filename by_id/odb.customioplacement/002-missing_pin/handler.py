def handle(step, exception, caplog):
    assert exception is None, "A pin missing from the design raised an exception"
    assert (
        "not found in design but found in config" in caplog.text
    ), "no message printed about missing pin"

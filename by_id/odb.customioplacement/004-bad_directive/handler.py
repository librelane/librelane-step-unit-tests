def handle(step, exception, caplog):
    assert exception is not None, "A bad configuration file did not raise an exception"

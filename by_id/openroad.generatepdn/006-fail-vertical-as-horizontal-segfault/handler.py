def handle(step, exception, caplog):
    assert exception is not None, "Check nodes didn't catch missing PDN"
    print(exception)

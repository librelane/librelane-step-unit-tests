def handle(step, exception, caplog):
    assert exception is not None, "Didn't fail on bad master"

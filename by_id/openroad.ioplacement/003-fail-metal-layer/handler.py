def handle(step, exception, caplog):
    assert exception is not None, "Didn't fail on unknown metal layer"
    error_msg = "[ERROR PPL-0051] Layer"
    assert error_msg in caplog.text, f"Didn't report error: {error_msg}"

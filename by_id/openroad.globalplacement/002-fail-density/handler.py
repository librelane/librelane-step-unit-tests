def handle(step, exception, caplog):
    assert exception is not None, "Didn't fail on too low density"
    error_msg = "[ERROR GPL-0302] Use a higher -density"
    assert error_msg in caplog.text, f"Didn't report {error_msg}"

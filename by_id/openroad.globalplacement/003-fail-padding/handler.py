def handle(step, exception, caplog):
    assert exception is not None, "Didn't fail on too low density"
    error_msg = "[ERROR GPL-0301] Utilization exceeds"
    assert error_msg in caplog.text, f"Didn't report {error_msg}"

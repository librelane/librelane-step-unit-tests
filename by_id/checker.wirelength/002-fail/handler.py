def handle(step, exception):
    error_msg = "Threshold-surpassing long wires found"
    assert error_msg in str(
        exception
    ), f"Different exception caught.\nExpected: {error_msg}\nFound:{str(exception)}"

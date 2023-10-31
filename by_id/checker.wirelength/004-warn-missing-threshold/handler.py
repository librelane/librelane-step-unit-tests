def handle(step, caplog):
    warning_msg = "Threshold for Threshold-surpassing long wires is not set"
    assert (
        warning_msg in caplog.text
    ), f"Different warning message reported.\nExpected: {warning_msg}\nFound: {caplog.text}"

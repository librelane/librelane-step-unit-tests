def handle(step, caplog):
    warning_msg = "The Threshold-surpassing long wires metric"
    assert (
        warning_msg in caplog.text
    ), f"Different warning message reported.\nExpected: {warning_msg}\nFound: {caplog.text}"

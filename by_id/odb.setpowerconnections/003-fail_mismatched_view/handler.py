def handle(step, caplog, exception):
    assert exception is not None, "No exception raised for mismatched views"
    assert (
        "the LEF and Verilog views of the module may be mismatched" in caplog.text
    ), "No diagnostic message printed for mismatched views"

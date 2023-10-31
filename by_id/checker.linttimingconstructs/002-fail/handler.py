def handle(step, exception):
    assert "Timing constructs found in the RTL" in str(
        exception
    ), f"Different exception caught: '{exception}'\n.Perhaps the error message changed?"

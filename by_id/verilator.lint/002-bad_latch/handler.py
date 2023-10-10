def handle(step):
    assert (
        step.state_out.metrics["design__inferred_latch__count"] == 1
    ), "Invalid latch count not properly detected"

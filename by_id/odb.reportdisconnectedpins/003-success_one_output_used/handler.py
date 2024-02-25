def handle(step):
    assert (
        step.state_out.metrics["design__disconnected_pin__count"] != 0
    ), "False negative on disconnected pins"
    assert (
        step.state_out.metrics["design__critical_disconnected_pin__count"] == 0
    ), "False positive on critical disconnected pins"

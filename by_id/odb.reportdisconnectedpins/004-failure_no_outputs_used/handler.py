def handle(step, caplog):
    assert (
        "No outputs of macro/instance 'ff' are connected- add it to IGNORE_DISCONNECTED_MODULES if this is intentional"
        in caplog.text
    ), "Did not warn about outputs of instance being unused"
    assert (
        step.state_out.metrics["design__disconnected_pin__count"] != 0
    ), "False negative on disconnected pins"

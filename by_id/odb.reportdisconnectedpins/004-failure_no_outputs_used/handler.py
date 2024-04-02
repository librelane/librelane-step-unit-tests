def handle(step, caplog, openroad_alerts):
    assert (
        "No outputs of macro/instance 'ff' are connected- add it to IGNORE_DISCONNECTED_MODULES if this is intentional"
        in ";".join(alert.message for alert in openroad_alerts)
    ), "no message printed about missing pin"
    assert (
        step.state_out.metrics["design__disconnected_pin__count"] != 0
    ), "False negative on disconnected pins"

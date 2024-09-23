from openlane.steps.checker import HoldViolations, SetupViolations


def handle(step):
    hold_violation_count = step.state_out.metrics[HoldViolations.metric_name]
    assert (
        hold_violation_count == 0
    ), f"Expected Hold Violations: 0, Found: {hold_violation_count}"
    setup_violation_count = step.state_out.metrics[SetupViolations.metric_name]
    assert (
        setup_violation_count == 0
    ), f"Expected Setup Violations: 0, Found: {setup_violation_count}"

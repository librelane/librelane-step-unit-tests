from openlane.steps.checker import HoldViolations, SetupViolations


def handle(step):
    hold_ws = step.state_out.metrics["timing__hold__ws__corner:nom_tt_025C_1v80"]
    assert hold_ws > 20, f"Expected Hold Worst Slack >20. Found: {hold_ws}"

def handle(step):
    error_count = step.state_out.metrics["design__lvs_error__count"]
    assert error_count == 0, f"LVS didn't pass. Found {error_count} errors"

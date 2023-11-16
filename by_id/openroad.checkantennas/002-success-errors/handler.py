def handle(step):
    assert (
        step.state_out.metrics["antenna__count"] > 0
    ), f"Expected > 0. Found: {step.metrics['antenna__count']}"

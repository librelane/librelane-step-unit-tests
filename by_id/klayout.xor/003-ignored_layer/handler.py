def handle(step):
    assert (
        step.state_out.metrics["design__xor_difference__count"] == 0
    ), "difference in ignored layer still counted"

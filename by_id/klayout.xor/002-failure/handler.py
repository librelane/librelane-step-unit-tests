def handle(step):
    assert (
        step.state_out.metrics["design__xor_difference__count"] == 1
    ), "difference not detected by XOR"

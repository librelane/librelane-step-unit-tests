def handle(step):
    assert (
        step.state_out.metrics["timing__unannotated_nets__count"] == 392
    ), f"Error: Expected timing__unannotated_nets__count 392: Found {step.state_out.metrics['timing__unannotated_nets__count']}"
    assert (
        step.state_out.metrics["timing__unannotated_nets_filtered__count"] == 68
    ), f"Error: Expected timing__unannotated_nets_filtered__count 68: Found {step.state_out.metrics['timing__unannotated_nets_filtered__count']}"

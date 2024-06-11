def handle(step):
    illegal_overlap_count = step.state_out.metrics["magic__illegal_overlap__count"]
    assert (
        illegal_overlap_count == 5
    ), "Failed to extract proper count for illegal overlaps"

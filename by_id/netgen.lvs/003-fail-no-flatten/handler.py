def handle(step):
    metric_name = "design__lvs_error__count"
    metric_value = step.state_out.metrics[metric_name]
    expected_value = 4

    assert (
        metric_value == expected_value
    ), f"Wrong value for '{metric_name}'. Expected: {expected_value}. Found {metric_value}"

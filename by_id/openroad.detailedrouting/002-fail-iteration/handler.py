from openlane.steps.checker import TrDRC


def handle(step):
    assert (
        step.state_out.metrics[TrDRC.metric_name] > 0
    ), "No DRC violations produced by detailed router"

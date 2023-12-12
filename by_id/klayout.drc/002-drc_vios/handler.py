from openlane.steps.checker import KLayoutDRC


def handle(step):
    drc_count = step.state_out.metrics[KLayoutDRC.metric_name]
    assert drc_count == 0, f"Expected DRC: 0, Found: {drc_count}"

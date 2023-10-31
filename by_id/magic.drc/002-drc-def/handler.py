from openlane.steps.checker import MagicDRC


def handle(step):
    drc_count = step.state_out.metrics[MagicDRC.metric_name]
    assert drc_count > 0, f"Expected DRC: > 0, Found: {drc_count}"
    assert (
        step.config["MAGIC_DRC_USE_GDS"] is False
    ), "MAGIC_DRC_USE_GDS is enabled. This test runs on DEF/LEF."

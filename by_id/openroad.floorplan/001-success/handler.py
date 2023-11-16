from typing import Optional, Tuple
from decimal import Decimal


from openlane.config.variable import Variable
from openlane.common import GenericDict


def handle(step):
    area = Variable(
        "DIE_AREA",
        Optional[Tuple[Decimal, Decimal, Decimal, Decimal]],
        'Specific die area to be used in floorplanning when `FP_SIZING` is set to `absolute`. Specified as a 4-corner rectangle "x0 y0 x1 y1".',
        units="µm",
        default=step.state_out.metrics["design__die__bbox"],
    )
    _, area = area.compile(GenericDict(), [], permissive_typing=True)
    assert (
        area == step.config["DIE_AREA"]
    ), f"Expected: {step.config['DIE_AREA']}. Found {area}"

#!/usr/bin/env python3
# Copyright 2020 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys

from openlane.scripts.odbpy.reader import click_odb, click
from openlane.scripts.odbpy.defutil import parse_obstructions


@click.command("verify_obstructions")
@click.option(
    "-O",
    "--obstructions",
    required=True,
    help="Format: layer llx lly urx ury, (microns)",
)
@click_odb
def verify_obstructions(reader, input_lefs, obstructions):
    obs_list = parse_obstructions(obstructions)
    dbu = reader.tech.getDbUnitsPerMicron()
    design_obstructions = reader.block.getObstructions()

    for obs in obs_list:
        layer = obs[0]
        bbox = obs[1]
        found = False
        bbox = [int(x * dbu) for x in bbox]
        for design_obstruction in design_obstructions:
            design_bbox = design_obstruction.getBBox()
            if (
                layer == design_bbox.getTechLayer().getName()
                and bbox[0] == design_bbox.xMin()
                and bbox[1] == design_bbox.yMin()
                and bbox[2] == design_bbox.xMax()
                and bbox[3] == design_bbox.yMax()
            ):
                found = True
                break

        if not found:
            print(f"[ERROR] obstruction {layer} {bbox} not found")
            sys.exit(1)


if __name__ == "__main__":
    verify_obstructions()

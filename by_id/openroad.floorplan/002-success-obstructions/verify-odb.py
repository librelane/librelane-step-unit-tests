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

from reader import click_odb, click


@click.command("verify_obstructions")
@click.option(
    "-O",
    "--obstructions",
    multiple=True,
    type=str,
    required=True,
)
@click_odb
def verify_obstructions(reader, input_lefs, obstructions):
    dbu = reader.tech.getDbUnitsPerMicron()
    design_obstructions = reader.block.getBlockages()

    print(obstructions)
    for obs in obstructions:
        obs = obs.split()
        bbox = [obs[0], obs[1], obs[2], obs[3]]
        found = False
        bbox = [int(float(x) * dbu) for x in bbox]
        for design_obstruction in design_obstructions:
            design_bbox = design_obstruction.getBBox()
            if (
                bbox[0] == design_bbox.xMin()
                and bbox[1] == design_bbox.yMin()
                and bbox[2] == design_bbox.xMax()
                and bbox[3] == design_bbox.yMax()
            ):
                found = True
                break

        if not found:
            print(f"[ERROR] obstruction {bbox} not found")
            sys.exit(1)


if __name__ == "__main__":
    verify_obstructions()

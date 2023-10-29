import os
from PIL import Image


def handle(step):
    image = os.path.join(step.step_dir, "out.png")

    with Image.open(image) as im:
        im.verify()

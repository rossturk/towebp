#!/usr/bin/env python3

import click
import os
from pathlib import Path

from PIL import Image

@click.command()
@click.argument("infile")
def towebp(infile):

    try:
        size = os.path.getsize(infile)
    except:
        print("Error: could not open", infile)
        exit(1)

    file_path = Path(infile)
    image = Image.open(file_path)

    webp_path = file_path.with_suffix(".webp")

    image.save(webp_path, "webp")
    print(f'{file_path} -> {webp_path} ✅')

if __name__ == "__main__":
    towebp(auto_envvar_prefix="TOWEBP")

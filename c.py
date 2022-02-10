#!/usr/bin/env python3
from PIL import Image
import glob
from pathlib import Path

cur_dir = Path('png').resolve()
for img in glob.glob(str(cur_dir / "*.png")):
    filename = Path(img).stem
    Image.open(img).save(str("bmp/"  + filename + ".bmp"))

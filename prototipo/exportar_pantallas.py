"""Recorta cada pantalla del prototipo a partir de la captura completa de la galería.

Uso: python exportar_pantallas.py <captura_completa.png> <rects.json> <prefijo> <carpeta_salida>
rects.json: lista de {id, x, y, w, h, label} en coordenadas de documento (CSS px).
"""
import json
import re
import sys
from pathlib import Path

from PIL import Image

full_png, rects_json, prefix, out_dir = sys.argv[1:5]
out = Path(out_dir)
out.mkdir(parents=True, exist_ok=True)

img = Image.open(full_png)
rects = json.loads(Path(rects_json).read_text(encoding="utf-8"))

# La captura puede tener escala (deviceScaleFactor); se infiere por el ancho del documento.
doc_width = max(r["x"] + r["w"] for r in rects) + 40
scale = img.width / doc_width if img.width > doc_width * 1.5 else 1


def slug(text):
    text = re.sub(r"^\d+\s*[·\-]\s*", "", text)
    text = text.lower()
    text = re.sub(r"[áàä]", "a", text)
    text = re.sub(r"[éèë]", "e", text)
    text = re.sub(r"[íìï]", "i", text)
    text = re.sub(r"[óòö]", "o", text)
    text = re.sub(r"[úùü]", "u", text)
    text = text.replace("ñ", "n")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text


for i, r in enumerate(rects, 1):
    box = tuple(int(v * scale) for v in (r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"]))
    crop = img.crop(box)
    name = f"{prefix}-{i:02d}-{slug(r['label'])}.png"
    crop.save(out / name, optimize=True)
    print(name)

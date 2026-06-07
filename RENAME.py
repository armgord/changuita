#!/usr/bin/env python3
"""
Renombrador de archivos para el scrapbook.
Uso: python RENAME.py <carpeta>
Ejemplo: python RENAME.py fotos
         python RENAME.py stickers
         python RENAME.py videos
"""
import os, sys

EXTS = {'.jpg','.jpeg','.png','.gif','.webp','.mp4','.mov','.avi','.mkv','.svg'}

if len(sys.argv) < 2:
    print("Uso: python RENAME.py <carpeta>")
    print("Carpetas válidas: fotos  stickers  videos  recortes  letras  pcb")
    sys.exit(1)

folder = sys.argv[1]
if not os.path.isdir(folder):
    print(f"Error: no existe la carpeta '{folder}'")
    sys.exit(1)

prefix_map = {
    'fotos':    'foto',
    'stickers': 'sticker',
    'videos':   'video',
    'recortes': 'recorte',
    'letras':   'letra',
    'pcb':      'pcb',
}
prefix = prefix_map.get(folder, folder)

files = sorted([f for f in os.listdir(folder)
                if os.path.splitext(f)[1].lower() in EXTS])

if not files:
    print(f"No se encontraron archivos de imagen/video en '{folder}'")
    sys.exit(1)

print(f"\nRenombrando {len(files)} archivos en '{folder}/':")
for i, fname in enumerate(files, 1):
    ext = os.path.splitext(fname)[1].lower()
    if ext == '.jpeg': ext = '.jpg'
    new_name = f"{prefix}{i}{ext}"
    old_path = os.path.join(folder, fname)
    new_path = os.path.join(folder, new_name)
    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"  {fname}  →  {new_name}")
    else:
        print(f"  {fname}  (sin cambio)")

print(f"\nListo. {len(files)} archivos renombrados.")

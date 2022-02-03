#!/usr/bin/env python3

import sys
import json
from psd_tools import PSDImage

def save_layer(layer, info, prefix=''):
    if not layer.is_visible():
        return

    if not layer.is_group():
        name = f"{prefix}{layer.name}"

        print(f"Saving {name}...", file=sys.stderr)
        layer.topil().save(f'{name}.png')
        info.append({'image': f'pack/{name}', 'position': {'x': layer.bbox[0], 'y': layer.bbox[1]}})
    else:
        for child in layer:
            save_layer(child, info, f"{layer.name}-")

def main():
    if len(sys.argv) < 2:
        print("Usage: cut.py image.psd", file=sys.stderr)
        return 1

    psd_name = sys.argv[1]
    psd = PSDImage.open(psd_name)

    info = []
    for layer in psd:
        save_layer(layer, info)

    print(json.dumps(info, indent=4))

if __name__ == '__main__':
    main()

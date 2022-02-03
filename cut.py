#!/usr/bin/env python3

from sys import argv
from psd_tools import PSDImage

def save_layer(layer, prefix=''):
    if not layer.is_visible():
        return

    if not layer.is_group():
        name = f"{prefix}{layer.name}.png"
        print(f"Saving {name}...")
        layer.topil().save(name)
    else:
        for child in layer:
            save_layer(child, f"{layer.name}-")

def main():
    if len(argv) < 2:
        print("Usage: cut.py image.psd")
        return 1

    psd_name = argv[1]
    psd = PSDImage.open(psd_name)

    for layer in psd:
        save_layer(layer)

if __name__ == '__main__':
    main()

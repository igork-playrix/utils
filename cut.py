#!/usr/bin/env python3

import sys
import json
import argparse
from psd_tools import PSDImage

def parseArgs():
    parser = argparse.ArgumentParser(description='Cut your psds with no Photoshop.')
    parser.add_argument('psd', help='a psd file to cut')
    parser.add_argument('-l', '--layer', help='cut only a specific layer')
    parser.add_argument('-p', '--pos', action='store_true', help="only show a positioning info, don't export images")
    parser.add_argument('-i', '--invisible', action='store_true', help='ignore visibility')
    return parser.parse_args()

def save_layer(layer, info, args, save=True, prefix=''):
    if not args.invisible and not layer.is_visible():
        return

    if args.layer != None and layer.name == args.layer:
        save = True

    if not layer.is_group():
        name = f"{prefix}{layer.name}"

        if not save: return

        if not args.pos:
            print(f"Saving {name}...", file=sys.stderr)
            layer.topil().save(f'{name}.png')

        info.append({'image': f'{name}', 'position': {'x': layer.bbox[0], 'y': layer.bbox[1]}})
    else:
        for child in layer:
            save_layer(child, info, args, save, f"{prefix}{layer.name}-")

def main():
    args = parseArgs()

    psd_name = args.psd
    psd = PSDImage.open(psd_name)

    info = []
    for layer in psd:
        save_layer(layer, info, args, args.layer == None)

    print(json.dumps(info, indent=4))

if __name__ == '__main__':
    main()

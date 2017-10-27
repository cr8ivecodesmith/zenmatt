#!/usr/bin/env python
import os
import subprocess as sp
import argparse

from pygments.styles import STYLE_MAP


DEFAULT_OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'pygments'
)


def main(target):
    for style in STYLE_MAP.keys():
        css_file = os.path.join(target, '{}.css'.format(style))
        out_str = (sp.check_output([
            'pygmentize', '-S', style, '-f', 'html',
        ])).decode('utf-8')
        with open(css_file, 'w') as fh:
            fh.write(out_str)
        print('Style created: {}'.format(css_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output-dir',
        '-O',
        metavar='PATH',
        default=DEFAULT_OUTPUT_DIR,
        help=('Path where the styles will be saved. '
              'Default: {}').format(DEFAULT_OUTPUT_DIR)
    )
    args = parser.parse_args()
    os.makedirs(args.output_dir, mode=0o755, exist_ok=True)
    main(args.output_dir)

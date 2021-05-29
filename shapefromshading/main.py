#     ShapeFromShading - Creating heightmaps out of 2D seal images.
#     Copyright (C) 2021
#     Joana Bergsiek, Leonard Geier, Lisa Ihde, Tobias Markus, Dominik Meier, Paul Methfessel
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import cv2
import argparse
import logging

from shapefromshading.optimize import optimize_parameters
from shapefromshading.tsai_shah_linera import tsai_shah
from shapefromshading.tsai_shah_linera_specular import tsai_shah_specular

def main():
    parser = argparse.ArgumentParser(description='Seal Shape From Shading out of Potsdam')
    parser.add_argument('source')
    parser.add_argument('-o', '--output', help="Filename to write to", default="out.png")
    parser.add_argument('-alg', '--algorithm', help="Shape from Shading Algorithm to use", default='tsai_shah_specular',
                        choices=['tsai_shah', 'tsai_shah_specular'])
    parser.add_argument('-s', '--slant', help="Slant of lighting source", default=-0.785)
    parser.add_argument('-t', '--tilt', help="Tilt of lighting source", default=1.4)
    parser.add_argument('-i', '--iterations', help="Iterations to run the algorithm through", default=10)
    parser.add_argument('-l', '--loglevel', help="Set debugging level. Use \"debug\" for highest details", default="critical")
    parser.add_argument('-opt', '--optimize', help="Optimize parameters using genetically algorithm", action="store_true")

    args = parser.parse_args()

    numeric_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.loglevel)
    logging.basicConfig(level=numeric_level)

    img = cv2.imread(args.source)

    if args.optimize:
        truth = cv2.imread('images/uni_big_heightmap.png')
        truth_greyscale = cv2.cvtColor(truth, cv2.COLOR_RGB2GRAY) / 255.0
        optimize_parameters(img, truth_greyscale, args)
    elif args.algorithm == 'tsai_shah_specular':
        result = tsai_shah_specular(img, args.slant, args.tilt, args.iterations)
    else:
        result = tsai_shah(img, args.slant, args.tilt, 10)
    cv2.imwrite(args.output, result)
    logging.info("Wrote " + args.output)

if __name__ == "__main__":
    main()

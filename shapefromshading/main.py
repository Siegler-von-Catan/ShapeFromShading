import cv2
import argparse

from shapefromshading.tsai_shah_linera import tsai_shah
from shapefromshading.tsai_shah_linera_specular import tsai_shah_specular

def main():
    parser = argparse.ArgumentParser(description='Seal Shape From Shading out of Potsdam')
    parser.add_argument('source')
    parser.add_argument('-o', '--output', help="Filename to write to", default="out.png")
    parser.add_argument('-alg', '--algorithm', help="Shape from Shading Algorithm to use", default='tsai_shah',
                        choices=['tsai_shah', 'tsai_shah_specular'])
    parser.add_argument('-s', '--slant', help="Slant of lighting source", default=-0.785)
    parser.add_argument('-t', '--tilt', help="Tilt of lighting source", default=1.4)
    parser.add_argument('-i', '--iterations', help="Iterations to run the algorithm through", default=10)

    args = parser.parse_args()

    img = cv2.imread(args.source)
    if args.algorithm == 'tsai_shah_specular':
        result = tsai_shah_specular(img, args.slant, args.tilt, args.iterations)
    else:
        result = tsai_shah(img, -0.785, 1.4, 10)
    cv2.imwrite(args.output, result)
    print("Wrote " + args.output)

if __name__ == "__main__":
    main()

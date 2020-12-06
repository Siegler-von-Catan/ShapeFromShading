import cv2
import argparse

from shapefromshading.tsai_shah_linera import tsai_shah

def main():
    parser = argparse.ArgumentParser(description='Seal Shape From Shading out of Potsdam')
    parser.add_argument('source')
    parser.add_argument('-o', '--output', help="Filename to write to", default="out.png")

    args = parser.parse_args()

    img = cv2.imread(args.source)
    result = tsai_shah(img, -0.785, 1.4, 10)
    cv2.imwrite(args.output, result)
    print("Wrote " + args.output)

if __name__ == "__main__":
    main()

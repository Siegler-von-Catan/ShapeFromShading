import cv2
import argparse

from shapefromshading.tsai_shah_linera import tsai_shah

def main():
    parser = argparse.ArgumentParser(description='Seal Shape From Shading out of Potsdam')
    parser.add_argument('source')

    args = parser.parse_args()

    img = cv2.imread(args.source)
    result = tsai_shah(img, -0.785, 1.4, 10)
    cv2.imwrite('out.png', result)
    print("Wrote out.png")

if __name__ == "__main__":
    main()

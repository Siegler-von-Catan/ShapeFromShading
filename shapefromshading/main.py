import cv2
from shapefromshading.tsai_mubarak_linera import tsai_mubarak

def main():
    print("Hello from the shape of shading algorithm")
    img = cv2.imread('test.png')
    result = tsai_mubarak(img)
    cv2.imwrite('out.png', result)
    print("Wrote out.png")

if __name__ == "__main__":
    main()

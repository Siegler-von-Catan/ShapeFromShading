import cv2

from shapefromshading.optimize import score


def test_score():
    heightmap = (
        cv2.cvtColor(cv2.imread("./images/uni_big_heightmap.png"), cv2.COLOR_RGB2GRAY)
        / 255.0
    )
    greyscale = (
        cv2.cvtColor(cv2.imread("./images/uni_big_greyscale.png"), cv2.COLOR_RGB2GRAY)
        / 255.0
    )
    assert score(heightmap, heightmap) == 0
    assert score(greyscale, greyscale) == 0

    # This is just to find if the score function get's changed
    assert score(heightmap, greyscale) == 0.20209237171705513

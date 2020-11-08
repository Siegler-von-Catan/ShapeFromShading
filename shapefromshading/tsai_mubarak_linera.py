# This implements the Shape From Shading algorithm from the paper
# Shape from shading using linear approximation
# by Ping-Sing Tsai and Mubarak Shah (1994)
# The naming of functions is also taken out of the paper, in case you wonder about the weird naming.

import cv2
import numpy as np
import math


def tsai_mubarak(image, tilt, slant, iterations):
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    heightmap = np.zeros(grayscale.shape)
    heightmap_prev = np.zeros(grayscale.shape)
    si = np.full(grayscale.shape, 0.01)
    si_prev = np.full(grayscale.shape, 0.01)


    ps = math.cos(tilt) * math.sin(slant) / math.cos(slant)
    qs = math.sin(tilt) * math.sin(slant) / math.cos(slant)
    Wn = 0.00000001
    height, width = grayscale.shape
    for iteration in range(iterations):
        print(iteration)
        for x in range(1, width):
            for y in range(1, height):
                p = heightmap_prev[y, x] - heightmap_prev[y, x - 1]
                q = heightmap_prev[y, x] - heightmap_prev[y - 1, x]
                pq = 1.0 + p * p + q * q
                pqs = 1.0 + ps * ps + qs * qs
                e = grayscale[y, x] / 255.0
                fZ = -1.0 * (e - max(0.0, (1 + p * ps + q * qs) / (
                        math.sqrt(1.0 + p * p + q * q) * math.sqrt(1.0 + ps * ps + qs * qs))))
                dfZ = -1.0 * ((ps + qs) / (math.sqrt(pq) * math.sqrt(pqs)) - (p + q) * (1.0 + p * ps + q * qs) / (
                        math.sqrt(pq * pq * pq) * math.sqrt(pqs)))
                Y = fZ + dfZ * heightmap[y, x]
                K = si_prev[y, x] * dfZ / (Wn + dfZ * si_prev[y, x] * dfZ)
                si[y, x] = (1.0 - K * dfZ) * si_prev[y, x]
                heightmap[y, x] = heightmap_prev[y, x] + K * (Y - dfZ * heightmap_prev[y, x])
        heightmap_prev = heightmap
        si = si_prev

    return heightmap


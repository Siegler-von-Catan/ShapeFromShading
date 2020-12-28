# This implements the Shape From Shading algorithm from the paper
# Shape from shading using linear approximation
# by Ping-Sing Tsai and Mubarak Shah (1994)
# The naming of functions is also taken out of the paper, in case you wonder about the weird naming.

import cv2
import numpy as np
import math


def tsai_shah_specular(image, tilt, slant, iterations):
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) / 255.0
    heightmap = np.zeros(grayscale.shape)
    heightmap_prev = np.zeros(grayscale.shape)
    si = np.full(grayscale.shape, 0.01)
    si_prev = np.full(grayscale.shape, 0.01)

    # Specular constants
    bisect_light_view = [0.1, 0, 1]
    H = bisect_light_view / np.linalg.norm(bisect_light_view)
    m = 1
    K_light = -10

    ps = math.cos(tilt) * math.sin(slant) / math.cos(slant)
    qs = math.sin(tilt) * math.sin(slant) / math.cos(slant)
    pqs = 1.0 + ps * ps + qs * qs
    ps_p_qs = ps + qs
    Wn = 0.0001
    height, width = grayscale.shape
    for iteration in range(iterations):
        print(iteration)

        cv2.imwrite('out' + str(iteration) + '.png', heightmap)

        zX = np.zeros(shape=(height, 1))
        hmX = np.concatenate((heightmap_prev[:, :-1], zX), axis=1)
        zY = np.zeros(shape=(1, width))
        hmY = np.concatenate((heightmap_prev[:-1, :], zY), axis=0)

        p = heightmap_prev - hmX
        q = heightmap_prev - hmY

        pq = 1.0 + p * p + q * q
        ppsqqs = 1.0 + p * ps + q * qs
        sqrt_pq_pqs = np.sqrt(pq * pqs)

        exponents = np.zeros(shape=heightmap.shape)
        for y in range(height):
            for x in range(width):
                nh = (p[y][x] * H[0] + q[y][x] * H[1] + H[2]) / np.sqrt(p[y][x] * p[y][x] + q[y][x] * q[y][x] + 1)
                alpha = np.arccos(nh)
                exponents[y][x] = - (alpha * alpha / m * m)
        fZ = grayscale - K_light * np.power(np.e, exponents)
        dfZ = -2.0 * K_light * np.power(np.e, exponents) * alpha / (m * m * np.sqrt(1- nh * nh)) * (H[0] + H[1] + H[2] - ((p* H[0] + q * H[1] + H[2]) * (p + q)/ pq)) * np.power(pq, -0.5)
        Y = fZ + dfZ * heightmap
        K = si_prev * dfZ / (Wn + dfZ * si_prev * dfZ)
        si = (1.0 - K * dfZ) * si_prev

        heightmap = heightmap_prev + K * (Y - dfZ * heightmap_prev)

        heightmap_prev = heightmap
        si_prev = si

    heightmap -= np.min(heightmap) # Put linear between 0 and 1
    heightmap /= np.max(heightmap)
    return heightmap * 255


#     ShapeFromShading - Creating heightmaps out of 2D seal images.
#     Copyright (C) 2021
#     Joana Bergsiek, Leonard Geier, Lisa Ihde, Tobias Markus, Dominik Meier, Paul Methfessel
#
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


# This implements the Shape From Shading algorithm from the paper
# Shape from shading using linear approximation
# by Ping-Sing Tsai and Mubarak Shah (1994)
# The naming of functions is also taken out of the paper, in case you wonder about the weird naming.

import cv2
import numpy as np
import math
import logging


def tsai_shah(image, tilt, slant, iterations):
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) / 255.0
    heightmap = np.zeros(grayscale.shape)
    heightmap_prev = np.zeros(grayscale.shape)
    si = np.full(grayscale.shape, 0.01)
    si_prev = np.full(grayscale.shape, 0.01)


    ps = math.cos(tilt) * math.sin(slant) / math.cos(slant)
    qs = math.sin(tilt) * math.sin(slant) / math.cos(slant)
    pqs = 1.0 + ps * ps + qs * qs
    ps_p_qs = ps + qs
    Wn = 0.00000001
    height, width = grayscale.shape
    for iteration in range(iterations):
        logging.debug(iteration)

        if logging.DEBUG >= logging.root.level:
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
        fZ = -1.0 * (grayscale - np.clip(ppsqqs, 0.0, None) / sqrt_pq_pqs)
        dfZ = -1.0 * (ps_p_qs / sqrt_pq_pqs - (p + q) * ppsqqs / (pq * sqrt_pq_pqs))
        Y = fZ + dfZ * heightmap
        K = si_prev * dfZ / (Wn + dfZ * si_prev * dfZ)
        si = (1.0 - K * dfZ) * si_prev
        heightmap = heightmap_prev + K * (Y - dfZ * heightmap_prev)

        heightmap_prev = heightmap
        si_prev = si

    return heightmap


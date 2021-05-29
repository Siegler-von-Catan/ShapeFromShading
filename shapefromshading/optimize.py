from numbers import Number

import numpy as np

from skimage.metrics import structural_similarity

from geneticalgorithm import geneticalgorithm

from .tsai_shah_linera_specular import tsai_shah_specular

def optimize_parameters(test_image, ground_truth_image, args):
    def function_to_optimize(X):
        slant = X[0]
        tilt = X[1]
        heightmap = tsai_shah_specular(test_image, tilt, slant, args.iterations)
        return score(heightmap, ground_truth_image)

    variable_boundaries = np.array([[-1, 1]] * 2)
    model = geneticalgorithm(function=function_to_optimize, dimension=2, variable_type='real', variable_boundaries=variable_boundaries)
    model.run()

# Return the similarity score of these pictures
# in interval from [0, 1] where 0 is very similar
def score(test_image, ground_truth_image) -> Number:
    # Goes from -1.0 to 1.0
    similarity = structural_similarity(test_image, ground_truth_image)
    return (1 - similarity) / 2

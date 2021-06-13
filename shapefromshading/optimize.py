from numbers import Number

import numpy as np

from skimage.metrics import structural_similarity

from geneticalgorithm import geneticalgorithm

from .tsai_shah_linera_specular import tsai_shah_specular


def optimize_parameters(test_image, ground_truth_image, args):
    def function_to_optimize(X):
        slant = X[0]
        tilt = X[1]
        # print(f"Try {slant} and {tilt} now")
        heightmap = tsai_shah_specular(test_image, tilt, slant, 3)
        return score(heightmap, ground_truth_image)

    algorithm_parameters = {
        "max_num_iteration": None,
        "population_size": 5,
        "mutation_probability": 0.1,
        "elit_ratio": 0.01,
        "crossover_probability": 0.5,
        "parents_portion": 0.3,
        "crossover_type": "uniform",
        "max_iteration_without_improv": None,
    }

    variable_boundaries = np.array([[-1, 1]] * 2)
    model = geneticalgorithm(
        function=function_to_optimize,
        dimension=2,
        variable_type="real",
        variable_boundaries=variable_boundaries,
        algorithm_parameters=algorithm_parameters,
    )
    model.run()


# Return the similarity score of these pictures
# in interval from [0, 1] where 0 is very similar
def score(test_image, ground_truth_image) -> Number:
    # Goes from -1.0 to 1.0
    similarity = structural_similarity(test_image, ground_truth_image)
    return (1 - similarity) / 2

import numpy as np
from itertools import product


with open("inputs/day20.txt") as f:
    algorithm, image = f.read().split("\n\n")
    algorithm = np.array([int(pixel == "#") for pixel in algorithm.strip()])
    image = np.array([[int(pixel == "#") for pixel in line.strip()]
                     for line in image.split("\n")])


def enhance_image(image, algorithm, n_times):
    powers = 2 ** np.arange(9)[::-1].reshape(3, 3)

    for i in range(n_times):
        pad_val = 1 if (i % 2 and algorithm[0] == 1) else 0
        image = np.pad(image, pad_width=2, constant_values=pad_val)
        H, W = image.shape
        enhanced = np.zeros_like(image)

        for i, j in product(range(1, H - 1), range(1, W - 1)):
            kernel = image[i - 1: i + 2, j - 1: j + 2]
            index = (kernel * powers).sum()
            enhanced[i, j] = algorithm[index]
        image = enhanced[1:-1, 1:-1]

    return image


print(enhance_image(image, algorithm, n_times=2).sum())
print(enhance_image(image, algorithm, n_times=50).sum())

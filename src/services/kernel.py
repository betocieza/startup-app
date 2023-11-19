print(__doc__)
import numpy as np
from scipy.spatial.distance import pdist, cdist
from scipy.spatial.distance import squareform


def PUK_kernel(X,Y, sigma=.6, omega=0.6):
    # Compute the kernel matrix between two arrays using the Pearson VII function-based universal kernel.
    # Compute squared euclidean distance between each row element pair of the two matrices

    if X is Y :
        kernel = squareform(pdist(X, 'sqeuclidean'))
    else:
        kernel = cdist(X, Y, 'sqeuclidean')

    kernel = (1 + (kernel * 4 * np.sqrt(2**(1.0/omega)-1)) / sigma**2) ** omega
    kernel = 1/kernel

    return kernel



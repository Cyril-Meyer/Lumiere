import numpy as np


def mean(data, out=0, debug=False):
    if debug:
        print('mean input data', data.shape, data.dtype)

    if out == 0:
        data = np.mean(data, axis=(1, 2))
    elif out == 1 or out == 2:
        data = np.mean(data, axis=out)
    else:
        raise ValueError

    if debug:
        print('mean output data', data.shape, data.dtype)

    return data

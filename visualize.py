import numpy as np
import matplotlib.pyplot as plt


def convert_to_image(data, debug=False):
    if debug:
        print('convert_to_image input data', data.shape, data.dtype)

    if len(data.shape) == 2:
        size = data.shape[0]
        data = np.expand_dims(data, 0)
        data = np.repeat(data, size, axis=0)
    else:
        data = np.transpose(data, axes=[1, 0, 2])

    data = (data / 255.0).astype(np.float32)

    if debug:
        print('convert_to_image output data', data.shape, data.dtype)

    return data


def view_value(data, output=None):
    if output is None:
        plt.imshow(data)
        plt.show()
    else:
        plt.imsave(output, data)

import argparse
import convert
import aggregate
import visualize
import numpy as np


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-output', default=None)
    parser.add_argument('-aggregate_opt', default=0)
    parser.add_argument('-framerate', default=25)
    parser.add_argument('-debug', default=False)
    args = parser.parse_args()

    if str(args.input).endswith('.npy'):
        data = np.load(str(args.input))
    else:
        data = convert.read_video(str(args.input), int(args.framerate))

    data = aggregate.mean(data, out=int(args.aggregate_opt), debug=bool(args.debug))
    data = visualize.convert_to_image(data, debug=bool(args.debug))
    visualize.view_value(data, output=str(args.output))

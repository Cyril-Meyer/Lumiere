import argparse
import time
import numpy as np
import cv2


def read_video(filename, framerate):
    t0 = time.time()

    cap = cv2.VideoCapture(filename)

    if not cap.isOpened():
        raise FileNotFoundError

    count = 0
    video = []

    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_FRAMES, count * framerate)
        ret, frame = cap.read()

        if not ret:
            break

        video.append(frame)
        count = count + 1

    cap.release()

    t1 = time.time()

    video = np.array(video)

    print(f'read_video time : {t1 - t0}')
    print(f'read_video shape, min, max : {video.shape} {video.min()} {video.max()}')

    return video


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-output', default='out')
    parser.add_argument('-framerate', default=25)
    args = parser.parse_args()

    print("input filename :", args.input)
    print("output filename :", args.output)
    print("capture framerate :", args.framerate)

    data = read_video(args.input, int(args.framerate))
    np.save(args.output, data)

import os
import sys
import time
import socket
import json
import datetime

import cv2
import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file",
                        required=False,
                        default='',
                        type=str,
                        help="Path to CSV file")
    args = parser.parse_args()
    return args


def visualize(args):
    # first latency is usually larger, possibly warm-up
    array_ov = np.genfromtxt('data/openvino_latency_faster_rcnn.csv', delimiter=',')[1:]
    array_tf = np.genfromtxt('data/tf_latency_faster_rcnn.csv', delimiter=',')[1:]
    # array_ov = np.genfromtxt('data/openvino_latency_ssd.csv', delimiter=',')[1:]
    # array_tf = np.genfromtxt('data/tf_latency_ssd.csv', delimiter=',')[1:]

    avg_ov = np.average(array_ov)
    avg_tf = np.average(array_tf)
    print('Average OpenVINO:', avg_ov, 'Average TF:', avg_tf, 'Gain:', (avg_tf/avg_ov), 'times')

    plt.plot(array_ov)
    plt.plot(array_tf)
    plt.show()


def main():
    # Grab command line args
    args = parse_args()
    # Visualize according to command line args
    visualize(args)


if __name__ == '__main__':
    main()

# coding=UTF-8
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def PlotPath(keyframes):
    fig = plt.figure('ch2')
    ax = Axes3D(fig)

    # lidar pose
    p00, = ax.plot(keyframes[:, 0], keyframes[:, 1], keyframes[:, 2], 'y-')

    plt.title("Pose 3d trajectory", fontsize=16)
    plt.grid()

    plt.show()


def LoadMappingTxt(filepath):
    keyframes = np.loadtxt(filepath)
    PlotPath(keyframes)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please input vaild param !!!')
        exit(1)
    else:
        path = sys.argv[1]
        LoadMappingTxt(path)
        exit(1)
        exit(1)

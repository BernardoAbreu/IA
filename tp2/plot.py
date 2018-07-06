#!/usr/bin/env  python

import argparse
import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
from pandas import DataFrame
from sys import argv

from matplotlib.legend_handler import HandlerLine2D

params = {
    'legend.fontsize': 'x-large',
    'figure.figsize': (20, 15),
    'axes.labelsize': 'x-large',
    'axes.titlesize': 'large',
    'xtick.labelsize': 'x-large',
    'ytick.labelsize': 'x-large'
}
plt.rcParams.update(params)


def loadtxt(file, delimiter=','):
    with open(file, 'r') as f:
        return np.array([list(map(float, line[:-1].split(delimiter)))
                        for line in f])


def line_mean_plot(a_l, y_label, labels, save=''):
    plt.rcParams.update(params)
    fig = plt.figure(figsize=(19, 11))
    ax = fig.add_subplot(111)

    list_of_means = []
    for a in a_l:
        means = []
        for column in a.T:
            means.append(np.mean(column))
        a_means = np.array(means)
        list_of_means.append(a_means)
        print(a_means)
    
    # plt.plot(np.arange(len(a_means)), a_means)
    plt.xlabel('Iterations', fontsize=48)
    plt.ylabel(y_label.title().replace('_', ' '), fontsize=48)
    plt.title(y_label.title().replace('_', ' ') + ' x Iterations', fontsize=48)
    ax.tick_params('both', labelsize=40)
    plt.grid(True)

    print(labels)
    line1 = None
    for mean, d in zip(list_of_means, labels):
        line1, = plt.plot(mean, label=str(d))

    plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)}, fontsize=34)
    # line1, = plt.plot(a_means, label=str(d))

    if save:
        print('saving to ' + save)
        plt.savefig(save + '_line_mean.eps', dpi=fig.dpi, format='eps')
    else:
        plt.show()


def line_plot(a, y_label, save=''):
    plt.plot(np.arange(len(a)), a)
    plt.xlabel('iterations')
    plt.ylabel(y_label.title())
    plt.title(y_label.title() + ' x Iterations')
    plt.grid(True)

    if save:
        print('saving to ' + save)
        plt.savefig(save + '_line.eps', dpi=300, format='eps')
    plt.show()


def boxplot(a, y_label, save=''):
    fig = plt.figure(figsize=(19, 5))
    plt.locator_params(axis='x', nticks=10)
    df = DataFrame(a)
    plt.figure()
    df.boxplot().set_xticklabels(
        [str(i) if i % 5 == 0 else '' for i in range(101)])

    plt.xlabel('Iterations')
    plt.ylabel(y_label.title().replace('_', ' '))
    plt.title(y_label.title().replace('_', ' ') + ' x Iterations')
    plt.grid(True)
    plt.tight_layout()

    if save:
        print('saving to ' + save)
        plt.savefig(save + '_boxplot.eps', dpi=fig.dpi, format='eps')


if __name__ == '__main__':
    print('running')
    parser = argparse.ArgumentParser()
    parser.add_argument('dirs', nargs='+')
    parser.add_argument('-i', '--input', required=True, help='Input file.')
    parser.add_argument('-o', '--output', help='Output file.')
    parser.add_argument('-t', '--plot-type', help='Plot type.', default='mean')

    args = parser.parse_args()

    dirs = args.dirs
    in_file = args.input
    a_list = [loadtxt('%s/%s' % (d, in_file)) for d in dirs]
    labels = [d.split('/')[-1] for d in dirs]

    label_title = in_file.split('__')[-1].split('.')[0]
    outputfolder = (args.output + label_title) if args.output else ''
    print(outputfolder)
    if args.plot_type == 'boxplot':
        boxplot(a_list, label, outputfolder)
    elif args.plot_type == 'mean':
        line_mean_plot(a_list, label_title, labels, outputfolder)
    elif args.plot_type == 'line':
        line_plot(a_list, label)

    # print argv
    # label = argv[1]
    # outfile = argv[2]

    # fig = plt.figure(figsize=(19, 11))
    # ax = fig.add_subplot(111)
    # plt.grid(True)

    # if label != 'test':
    #     plt.xlabel('Iterations')
    #     plt.ylabel(label.title())
    #     plt.title(label.title() + ' x Iterations')
    #     if 'crossss' in label:
    #         mm = []

    #         for i in argv[3:]:
    #             print i
    #             a = loadtxt(i)
    #             size = loadtxt(i.replace('__cross_best', '__cross_size')
    #                             .replace('__cross_worse', '__cross_size'))
    #             c = np.divide(a, size)
    #             means = []
    #             for column in c.T:
    #                 means.append(np.mean(column))
    #             mm.append(np.array(means))

    #         # line1, = plt.plot(mm[0][1:], label='500')

    #         line1 = None
    #         for m, d in zip(mm, [3, 7]):
    #             line1, = plt.plot(m, marker='o', label=str(d))

    #         plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

    #         # figure.set_size_inches(20, 15)
    #         plt.savefig(outfile + '_' + label + '_mean.png', dpi=fig.dpi)
    #         plt.show()
    #     else:
    #         mm = []

    #         for i in argv[3:]:
    #             print i
    #             a = loadtxt(i)
    #             means = []
    #             for column in a.T:
    #                 means.append(np.mean(column))
    #             mm.append(np.array(means))

    #         # line1, = plt.plot(mm[0][1:], label='500')

    #         line1 = None
    #         for m, d in zip(mm, #['k=2', 'k=3', 'k=7']):
    #                             ['best k=2', 'mean k=2','worst k=2',
    #                             'best k=3', 'mean k=3','worst k=3',
    #                             'best k=7', 'mean k=7','worst k=7']):
    #             line1, = plt.plot(m, label=str(d))

    #         ax.set_yscale('log')

    #         plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

    #         # figure.set_size_inches(20, 15)
    #         plt.savefig(outfile + '_' + label + '_mean.png', dpi=fig.dpi)
    #         plt.show()

    # else:
    #     plt.xlabel('Seed')
    #     plt.ylabel('Best fitness')
    #     plt.title('Best fitness x Seed')
    #     mm = []
    #     testbest = []

    #     for i in argv[3:]:
    #         print i
    #         a = loadtxt(i)
    #         test = loadtxt(i.replace('__best', '__test_best'))
    #         mm.append(a[:, -1])
    #         testbest.append(test)

    #     print len(mm)
    #     line1 = None
    #     for m, t in zip(mm, testbest):
    #         line1, = plt.plot(list(range(1, 31)), m, marker='o',
    #                           label='Treino')
    #         line4, = plt.plot(list(range(1, 31)), t, marker='x',
    #                           label='Teste')

    #     plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

    #     plt.savefig(outfile + '_' + label + '_test.png', dpi=fig.dpi)
    #     plt.show()

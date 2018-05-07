#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dtypes = {'Total Cost': float,
          'Expanded States': int,
          'Execution time': float}


def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            ip, fp, cost, exp_states, exec_time = line.rstrip().split(';')
            data.append([ip, fp, float(cost), int(exp_states),
                         float(exec_time)])
        return data


def main(map_folder):
    map_name = map_folder.split('/')[-2].split('.')[0]

    astar_manhat_filename = map_folder + 'astar_manhattan_stats' + '_sorted'
    astar_oct_filename = map_folder + 'astar_octile_stats' + '_sorted'
    bg_filename = map_folder + 'bg_stats' + '_sorted'
    ucs_filename = map_folder + 'ucs_stats' + '_sorted'
    ids_filename = map_folder + 'ids_stats' + '_sorted'

    a_manhat = pd.read_csv(astar_manhat_filename, sep=';', dtype=dtypes)
    a_oct = pd.read_csv(astar_oct_filename, sep=';', dtype=dtypes)
    bg = pd.read_csv(bg_filename, sep=';', dtype=dtypes)
    ucs = pd.read_csv(ucs_filename, sep=';', dtype=dtypes)
    ids = pd.read_csv(ids_filename, sep=';', dtype=dtypes)

    # with open('astar_manhat' + '_points', 'w') as f:
    #     f.write('\n'.join(a_manhat['Initial Point'] + ';' + a_manhat['Final Point']))

    # with open('a_oct' + '_points', 'w') as f:
    #     f.write('\n'.join(a_oct['Initial Point'] + ';' + a_oct['Final Point']))

    # with open('bg' + '_points', 'w') as f:
    #     f.write('\n'.join(bg['Initial Point'] + ';' + bg['Final Point']))

    # with open('ucs' + '_points', 'w') as f:
    #     f.write('\n'.join(ucs['Initial Point'] + ';' + ucs['Final Point']))

    # with open('ids' + '_points', 'w') as f:
    #     f.write('\n'.join(ids['Initial Point'] + ';' + ids['Final Point']))

    a_manhat[:40:2].to_csv('astar_manhattan_stats_' + map_name + '.csv', sep=';')
    a_oct[:40:2].to_csv('astar_octile_stats_' + map_name + '.csv', sep=';')
    bg[:40:2].to_csv('bg_stats_' + map_name + '.csv', sep=';')
    ucs[:40:2].to_csv('ucs_stats_' + map_name + '.csv', sep=';')
    ids[:40:2].to_csv('ids_stats_' + map_name + '.csv', sep=';')

    diff_index = [i for i, (m, o) in enumerate(zip(a_manhat['Total Cost'],
                                                   a_oct['Total Cost']))
                  if m != o]
    print(diff_index)
    metric = 'Total Cost'
    # # metric = 'Expanded States'
    # metric = 'Execution time'

    a_manhat.loc[diff_index].to_csv('astar_manhattan_diff' + map_name + '.csv',
                                    sep=';')
    a_oct.loc[diff_index].to_csv('astar_octile_diff' + map_name + '.csv',
                                 sep=';')

    ax = pd.concat([a_manhat[metric][diff_index].rename('A* Manhattan'),
                    a_oct[metric][diff_index].rename('A* Octile'),
                    ],
                   axis=1).plot.bar(title=metric)
    ax.set_xticklabels(range(len(diff_index)))
    plt.ylabel('Cost')
    fig = ax.get_figure()
    fig.savefig('images/' + metric + map_name + 'diff.pdf')

    # # gra = pd.concat([
    # #                 bg[metric][:].rename('BG'),
    # #                 a_manhat[metric][:].rename('A* Manhattan'),
    # #                 a_oct[metric][:].rename('A* Octile'),
    # #                 ucs[metric][:].rename('UCS'),
    # #                 ids[metric][:].rename('IDS')
    # #                 ],
    # #                 axis=1).plot.bar(title=metric)

    # log = False
    # # log = True
    # ax = pd.concat([
    #                bg[metric][:40:2].rename('BG'),
    #                a_oct[metric][:40:2].rename('A* Octile'),
    #                a_manhat[metric][:40:2].rename('A* Manhattan'),
    #                # ucs[metric][:40:2].rename('UCS'),
    #                # ids[metric][:40:2].rename('IDS')
    #                ],
    #                axis=1).plot.bar(title=metric,
    #                                 # )
    #                                 logy=log)
    # ax.set_xticklabels(range(20))
    # plt.ylabel('Seconds')
    # # plt.title(metric, fontsize=16)
    # fig = ax.get_figure()
    # fig.savefig('images/' + metric + map_name + "_heuristic" +
    #             ('log' if log else '') + '.pdf')
    plt.show()


if __name__ == '__main__':
    map_folder = sys.argv[1]
    main(map_folder)

import curses
import time


class Visu(object):

    def __init__(self):
        self.mywindow = curses.initscr()

    def init_screen(self, matrix):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                self.mywindow.addstr(i, j, str(matrix[i][j]))
        self.mywindow.refresh()
        time.sleep(0.5)

    def update_coord(self, coord, s):
        self.mywindow.addstr(coord.x, coord.y, s)
        self.mywindow.refresh()
        time.sleep(0.1)

    def close(self):
        curses.endwin()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

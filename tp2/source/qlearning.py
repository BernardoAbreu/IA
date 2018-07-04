import random
from stats import Stats


class QLearning(object):
    def __init__(self, maze, alpha, discount, iterations,
                 epsilon=0.2, seed=None):
        self.__alpha = alpha
        self.__discount = discount
        self.__iterations = iterations
        self.__maze = maze
        self.__actions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        self.__epsilon = epsilon

        self.__q = self.__initialize_q()
        self.__valid_states = self.__initialize_valid_states()

        random.seed(seed)

        self.stats = Stats()

    def __initialize_q(self):
        r = {'0': [10.], '&': [-10.], '-': [0.], '#': [0.]}

        rows, cols = len(self.__maze), len(self.__maze[0])
        return [[r[self.__maze[i][j]] * 4 for j in range(cols)]
                for i in range(rows)]

    def __initialize_valid_states(self):
        rows, cols = len(self.__maze), len(self.__maze[0])
        return [(i, j) for i in range(rows) for j in range(cols)
                if self.__maze[i][j] == '-']

    def __is_terminal(self, s):
        return self.__maze[s[0]][s[1]] in ('0', '&')

    def __get_reward(self, s):
        position = self.__maze[s[0]][s[1]]
        return -1. if position == '-' else (10. if position == '0' else -10.)

    def __initialize_state(self):
        return random.choice(self.__valid_states)

    def __choose_action(self, s):
        if random.random() < self.__epsilon:
            return random.randrange(len(self.__actions))
        else:
            return max(enumerate(self.__q[s[0]][s[1]]), key=lambda x: x[1])[0]

    def __take_action(self, s, a):
        action = self.__actions[a]
        next_s = (s[0] + action[0], s[1] + action[1])
        return s if self.__maze[next_s[0]][next_s[1]] == '#' else next_s

    def __update_q(self, s, a, next_s):
        lr = self.__alpha
        y = self.__discount
        r = self.__get_reward(s)
        cur_q = self.__q[s[0]][s[1]][a]
        next_q = max(self.__q[next_s[0]][next_s[1]])

        self.__q[s[0]][s[1]][a] += lr * (r + y * next_q - cur_q)

    def save_stats(self, out_file):
        self.stats.dump_to_file(out_file)

    def run(self):
        episode = 0
        iteration = 0
        while True:
            state = self.__initialize_state()
            while not self.__is_terminal(state):
                self.stats.add_data(self.__q)

                if iteration >= self.__iterations:
                    return self.__q

                action = self.__choose_action(state)
                next_state = self.__take_action(state, action)
                self.__update_q(state, action, next_state)
                iteration += 1
                state = next_state

            episode += 1

import random


class QLearning(object):
    def __init__(self, maze, alpha, discount, iterations, seed=None):
        self.__alpha = alpha
        self.__discount = discount
        self.__iterations = iterations
        self.__maze = maze
        self.__actions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        self.__epsilon = 0.2
        random.seed(seed)

        # self.__q = [[[.0, .0, .0, .0] for e in line] for line in maze]
        self.__initialize_q()
        self.__valid_states = []

        for i, line in enumerate(maze):
            for j, element in enumerate(line):
                if element == '-':
                    self.__valid_states.append((i, j))

    def __initialize_q(self):
        self.__q = []
        for i, line in enumerate(self.__maze):
            cur_line = []
            for j, element in enumerate(line):
                if element == '0':
                    cur_line.append([10.0, 10.0, 10.0, 10.0])
                if element == '&':
                    cur_line.append([-10.0, -10.0, -10.0, -10.0])
                else:
                    cur_line.append([.0, .0, .0, .0])
            self.__q.append(cur_line)

    def __is_terminal(self, s):
        return self.__maze[s[0]][s[1]] in ('0', '&')

    def __get_reward(self, s):
        position = self.__maze[s[0]][s[1]]
        return -1 if position == '-' else (10 if position == '0' else -10)

    def __initialize_state(self):
        # return (1, 3)
        return random.choice(self.__valid_states)

    def __choose_action(self, s):
        # return 0
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

    def run(self):
        episode = 0
        iteration = 0
        while True:
            state = self.__initialize_state()
            while not self.__is_terminal(state):
            # while True:
                # print_q(self.__q)
                if iteration >= self.__iterations:
                    return self.__q

                action = self.__choose_action(state)
                next_state = self.__take_action(state, action)
                self.__update_q(state, action, next_state)
                iteration += 1
                # if self.__is_terminal(state):
                    # break
                state = next_state

            episode += 1

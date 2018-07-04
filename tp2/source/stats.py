

class Stats(object):
    """ Stores and calculates statistics. """
    def __init__(self):
        self.reset()

    def add_data(self, q):
        cur_max_sum = 0
        cur_total_sum = 0
        for line in q:
            for element in line:
                cur_max_sum += max(element)
                cur_total_sum += sum(element)
        self.__total_max_sum.append(cur_max_sum)
        self.__total_sum.append(cur_total_sum)

    def reset(self):
        self.__total_sum = []
        self.__total_max_sum = []

    def dump_to_file(self, out_file):
        with open(out_file + '__q_max_sum.csv', 'a') as f:
            f.write(','.join(map(str, self.__total_max_sum)) + '\n')
        with open(out_file + '__q_total_sum.csv', 'a') as f:
            f.write(','.join(map(str, self.__total_sum)) + '\n')

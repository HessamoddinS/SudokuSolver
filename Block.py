class Block():

    def __init__(self, number, row, column, box_num):
        self._number = number
        self._row = row
        self._column = column
        self._box_num = box_num
        self._possible_nums = []

    def get_num(self):
        return self._number

    def set_num(self, number):
        self._number = number

    def set_poss_to_num(self):
        self._number = self._possible_nums[0]

    def is_empty(self):
        return self._number == 0

    def get_row(self):
        return self._row

    def get_column(self):
        return self._column

    def get_box_num(self):
        return self._box_num

    def set_poss(self, numbers):
        self._possible_nums = numbers

    def get_poss(self):
        return self._possible_nums

    def add_poss(self, number):
        self._possible_nums.append(number)

    def remove_poss(self, number):
        self._possible_nums.remove(number)

    def put_poss(self):
        self.set_num(self._possible_nums.pop())

    def get_poss_size(self):
        return len(self._possible_nums)

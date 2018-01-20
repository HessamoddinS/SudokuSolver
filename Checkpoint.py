import copy

class Checkpoint:
    
    def __init__(self, blocks):
        self._blocks = blocks
        self._rows = []
        self._columns = []
        self._boxes = []
        self._empty = 0
    
    def row_list_maker(self):
        self._rows = []
        for i in range(9):
            row = []
            for block in self._blocks:
                if block.get_row() == i:
                    if block.get_num() != 0:
                        row.append(block.get_num())
            self._rows.append(row)
    
    def column_list_maker(self):
        self._columns = []
        for i in range(9):
            column = []
            for block in self._blocks:
                if block.get_column() == i:
                    if block.get_num() != 0:
                        column.append(block.get_num())
            self._columns.append(column)
    
    def box_list_maker(self):
        self._boxes = []
        for i in range(9):
            box = []
            for block in self._blocks:
                if block.get_box_num() == i:
                    if block.get_num() != 0:
                        box.append(block.get_num())
            self._boxes.append(box)
    
    def possible_nums(self):
        for block in self._blocks:
            numbers = []
            if block.get_num() == 0:
                for i in range(1, 10):
                    if i not in self._rows[block.get_row()]:
                        if i not in self._columns[block.get_column()]:
                            if i not in self._boxes[block.get_box_num()]:
                                numbers.append(i)
                block.set_poss(numbers)
                
    def empty_block_check(self):
        self._empty = 0
        for block in self._blocks:
            if block.get_num() == 0:
                self._empty += 1
    
    def check(self):
        checkpoint = self
        self.empty_block_check()
        if self._empty > 0:
            self.row_list_maker()
            self.column_list_maker()
            self.box_list_maker()
            self.possible_nums()
            min_poss = -1
            for block in self._blocks:
                if (min_poss == -1 or block.get_poss_size() <= min_poss) and block.get_num() == 0:
                    min_poss = block.get_poss_size()
            if min_poss == 1:
                for block in self._blocks:
                    if block.get_poss_size() == 1:
                        block.put_poss()
                        break
                self._blocks = self.check()
            elif min_poss == 0:        
                self._blocks = None
            else:
                blocks_copy = []
                for block in self._blocks:
                    if block.get_poss_size() == min_poss:
                        guess_block = block
                for i in range(min_poss):                  
                    guess_block.put_poss()
                    blocks_copy = copy.deepcopy(self._blocks)
                    blocks_copy[guess_block.get_row() * 9 + guess_block.get_column()].set_poss([])
                    checkpoint = Checkpoint(blocks_copy)
                    c_blocks = checkpoint.check()
                    if c_blocks != None:
                        break
                self._blocks = c_blocks
        return checkpoint._blocks
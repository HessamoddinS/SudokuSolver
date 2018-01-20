from Block import *
from Checkpoint import *

def read_file(file_name):
    file = open(file_name, 'r')
    blocks = []
    row = 0
    for line in file:
        line = line.strip()
        for column in range(0, len(line)):
            if row < 3:
                box_num = 0
            elif row < 6:
                box_num = 3
            else:
                box_num = 6
            if column > 2:
                box_num += 1
            if column > 5:
                box_num += 1
            blocks.append(Block(int(line[column]), row, column, box_num))
        row += 1
    return blocks

checkpoint = Checkpoint(read_file("Sudoku3.txt"))
blocks = checkpoint.check();
row_print = ""
for block in blocks:
    row_print += str(block.get_num())
    if block.get_column() == 8:
        row_print += "\n"
print(row_print)
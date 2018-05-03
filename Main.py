from Block import *
from Checkpoint import *
import sys


def read_file(file):
    blocks = []
    row = 0
    for line in file:
        line = line.strip()
        if len(line) < 9:
            return None
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
            try:
                blocks.append(Block(int(line[column]), row, column, box_num))
            except:
                return None
        row += 1
        if row == 9:
            return blocks
    return None

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        try:
            file = open(sys.argv[i], 'r')
            read = read_file(file)
            file.close()
            if read is not None:
                checkpoint = Checkpoint(read)
                blocks = checkpoint.check()
                if blocks is not None:
                    row_print = ""
                    for block in blocks:
                        row_print += str(block.get_num())
                        if block.get_column() == 8:
                            row_print += "\n"
                    print(row_print)
                else:
                    print(sys.argv[i] + " is not a correct Sudoku")
            else:
                print(sys.argv[i] +
                      " must have 9 lines, each line having 9 digits")
        except:
            print(sys.argv[i] + " cannot be opened")
else:
    print("usage: foo file ...")
    exit(1)
exit(0)

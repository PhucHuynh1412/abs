tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(left, center, right):
    width = left + center + right
    for i in range(4):
        string = tableData[0][i].rjust(left) + tableData[1][i].rjust(center) + tableData[2][i].rjust(right)
        print(string)

print_table(10,10,10)



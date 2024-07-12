def safe_check(houses, row, column):
    count =0
    row_dec = 0 if row == 0 else 1
    row_inc = 1 if row == 9 else 2
    col_dec = 0 if column == 0 else 1
    col_inc = 1 if column == 9 else 2
    for i in range(row - row_dec, row + row_inc):
        for j in range(column - col_dec, column + col_inc):
            if houses[i][j] != 0:
                return False
            else:
                count+= 1
    if count > 0:
        return True
    return False


houses =[]
for row in range(10):
    temp =[]
    str = input()
    for col in str:
        if col.isdigit() :
            temp.append(int(col))
    houses.append(temp)
safe_count = 0
for row in range(10):
    for col in range(10):
        if houses[row][col] == 0:
            if safe_check(houses, row, col):
                safe_count += 1
print(safe_count)
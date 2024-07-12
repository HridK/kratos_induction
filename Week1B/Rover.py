def navigation(grid, start_position, commands):
    row,col = start_position
    row_cur,col_cur = start_position
    cmd_pos = 0
    while cmd_pos < len(commands):
        if (row > (len(grid)-1) or col >= len(grid[0]) or row < 0 or col < 0 ):
            break
        elif grid[row][col] == 'X':
            break
        else:
            row_cur,col_cur = row,col
            if commands[cmd_pos] == 'R':
                col+=1
            elif commands[cmd_pos] == 'L':
                col-=1
            elif commands[cmd_pos] == 'U':
                row-=1
            elif commands[cmd_pos] == 'D':
                row+=1

        cmd_pos+=1
    print(f'{col_cur},{row_cur}')


# __main__
dim = list(map(int,input().split(" ")))
grid = []
for row in range(dim[0]):
    grid.append(input().split(" "))
start_pos = list(map(int,input().split(" ")))
cmds = input().split(" ")
navigation(grid, start_pos, cmds)
import random
import msvcrt
import os
height = 4
width = 5
board = [[" "]*width for _ in range(height)]
directions = {"w":(0, -1), "s":(0, 1), "a":(-1, 0), "d":(1, 0)}
snake = [(1, 1), (1, 0)]
food = [(random.choice([0, 2, 3, 4, 5]), random.choice([0, 2, 3, 4, 5]))]
ate = True
length = 2

def spawnFood() -> tuple:
    global board
    empty = []
    for row in range(height):
        for column in range(width):
            if board[row][column]==" ":
                empty.append((column, row))
    nextFood = random.choice(empty)
    return nextFood


def render() -> None:
    global food
    global next
    global board
    global ate
    global length
    
    board = [[" "]*width for _ in range(height)]
    
    if snake[0] in food:
        ate = True
        newFood = spawnFood()
        food.append(newFood)
        food.remove(next)
        length += 1
        print(newFood)
    # for row in range(height):
    #     for column in range(width):
    #         if (column, row) in food:
    #             board[row][column] = "*"
    #         for part in snake:
    #             if (column, row) == part:
    #                 board[row][column] = "#"
    #             elif (column, row) == snake[0]:
    #                 board[row][column] = "O"
    else:
        board[snake[-1][0]][snake[-1][1]] = " "
        
    for part in snake:
        board[part[1]][part[0]] = "#"
    board[snake[0][1]][snake[0][0]] = "O"
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"+{'-'*(2*width+1)}+", end="")
    for i in board:
        print("\n| ", end="")
        for j in i:
            print(j, end=" ")
        print("|", end="")
    print(f"\n+{'-'*(2*width+1)}+")
    print(f"Length: {length}")

dir = "s"
while dir!="q":

    next = (snake[0][0]+directions[dir][0], snake[0][1]+directions[dir][1])
    if next[0] not in range(0, width) or next[1] not in range(0, height) or next in snake[:-1]:
        print("Crashed")
        break
    
    if dir!="q":
        snake.insert(0, next)
        if not ate:
            snake.pop()
            render()
        else:
            render()
            ate = False
            
    area = height*width
    if length == area:
        print("END!")
        break
    dir = msvcrt.getch().decode("utf-8") #input without enter

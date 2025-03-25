import random
#import msvcrt
import getch
import os

height = 6
width = 8

board = [[" "]*width for _ in range(height)]
directions = {"w":(0, -1), "s":(0, 1), "a":(-1, 0), "d":(1, 0)}
snake = [(1, 1), (1, 0)]
food = [(random.choice([0, 2, 3, 4, 5]), random.choice([0, 2, 3, 4, 5]))]#, (random.choice([0, 2, 3, 4, 5]), random.choice([0, 2, 3, 4, 5]))]
ate = True
length = len(snake)
running = True

for x, y in snake:
    board[x][y] = "#"
board[snake[0][0]][snake[0][1]] = "O"
    
def spawnFood() -> tuple:
    global board
    global running
    empty = []
    for row in range(height):
        for column in range(width):
            if board[row][column]==" ":
                empty.append((column, row))
    if len(empty) == 0:
        running = False
        return
    else:
        nextFood = random.choice(empty)
    return nextFood


def render() -> None:
    global food
    global next
    global board
    global ate
    global length
    for x in range(width):
        for y in range(height):
            if (x, y) not in snake and (x, y) not in food:
                board[y][x] = " "
    for x, y in food:
        board[y][x] = "*"
    for x, y in snake:
        board[y][x] = "#"
    board[snake[0][1]][snake[0][0]] = "O"
 
    if next in food:
        ate = True
        newFood = spawnFood()
        food.append(newFood)
        food.remove(next)
        length += 1
    else:
        board[snake[-1][1]][snake[-1][0]] = " "
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
while running:

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
    dir = getch.getch().decode("utf-8")
    if dir == "q":
        running = False

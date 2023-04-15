from tkinter import * 
import random

"""Game Constants"""
GAME_WIDTH = 500
GAME_HEIGHT = 500
SPACE_SIZE = 20
SNAKE_SIZE = 3
SNAKE_COLOR = 'blue'
FOOD_COLOR = 'yellow'
BACKGROUND_COLOR = 'black'
SPEED = 100

class Snake:
    def __init__(self):
        self.coordinates = []
        self.squares = []

        for i in range(SNAKE_SIZE):
            self.coordinates.append([0,0])

        for x , y in self.coordinates:
            self.squares.append(
                                canvas.create_rectangle(x,y,
                                                        x+SPACE_SIZE,
                                                        y+SPACE_SIZE,
                                                        fill=SNAKE_COLOR,
                                                        )
                                )
        

class Food:
    def __init__(self):

        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE))-1) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE))-1) * SPACE_SIZE

        self.coordinates = [x,y]
        self.oval=canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR, tags='XC12')

def next_turn(snake,food):

    global direction , SPEED , score ,canvas , label

    x , y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x, y))

    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        
        canvas.delete(food.oval)
        del food
        food=Food()
        score += 1
        SPEED -= 1

        label.config(text='score : {}'.format(score) )

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    if check_chok(snake):

        game_over()
        
        return

    window.after(SPEED, next_turn, snake, food)

def change_deriction(new):

    global direction


    if new == 'right':

        if direction != 'left':
            direction = new
    
    elif new == 'left':
    
        if direction != 'right':
            direction = new
    
    elif new == 'up':
    
        if direction != 'down':
            direction = new
    
    elif new == 'down':
    
        if direction != 'up':
            direction = new


def check_chok(snake):

    x , y = snake.coordinates[0]

    if 0 > x or x > GAME_WIDTH :
        
        return True
    
    elif 0 > y or y > GAME_HEIGHT:

        return True
    
    for i in snake.coordinates[1:]:

        if x == i[0] and y == i[1]:

            return True

    return False
    
    
def full_screen():
    print('full screen')
    pass

def game_over():
    global score

    canvas.delete(ALL)
    canvas.create_text(int(GAME_WIDTH/2), int(GAME_HEIGHT/2) , 
                       text='game over',
                       font=("arial",30,'bold'),
                       fill='red')
    canvas.create_text(int(GAME_WIDTH/2), int(GAME_HEIGHT/2)+30 , 
                       text='score: {}'.format(score),
                       font=("arial",15,'bold'),
                       fill='white')
    score = 0

direction = 'down'
score = 0

window = Tk()
window.title('Snake game')
window.resizable(False,False)
label = Label(window, text='score : {}'.format(score) , font=("arial",10,'bold'))
label.pack()
canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

snake = Snake()
food = Food()
window.bind('<Left>',lambda x : change_deriction('left'))
window.bind('<Up>',lambda x : change_deriction('up'))
window.bind('<Down>',lambda x : change_deriction('down'))
window.bind('<Right>',lambda x : change_deriction('right'))

window.bind('<f>',lambda x : full_screen())


next_turn(snake,food)


window.mainloop()

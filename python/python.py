import keyboard, time, os, random, sched, colorama, schedule


player_x = 1
player_y = 1


coin_x = random.randrange(0, 5)
coin_y = random.randrange(0, 5)

coins = 0

field = [[" ", " ", "#", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]

def game():
    global coins
    global player_x, player_y
    global field
    while True:
      print("coins:", coins)
      print("—————")
      field[player_x][player_y] = "@"
      for i in field:
        for j in range(len(i)):
          if j != 4:
            print(i[j], end = " ")
          else:
            print(i[j])
          
      time.sleep(0.2)
      os.system("cls")

def move_down():
  global player_x
  global player_y
  if player_x + 1 <= 4:
    field[player_x][player_y] = " "
    player_x += 1
  if player_x == coin_x and player_y == coin_y:
    coins += 1

def move_up():
  global coins
  global coin_x
  global coin_y
  global player_x
  global player_y
  if player_x - 1 >= 0:
     field[player_x][player_y] = " "
     player_x -= 1
  if player_x == coin_x and player_y == coin_y:
    coins += 1

def move_left():
  global coins
  global coin_x
  global coin_y
  global player_x
  global player_y
  if player_y + 1 <= 4:
    field[player_x][player_y] = " "
    player_y += 1
  if player_x == coin_x and player_y == coin_y:
    coins += 1

def move_right():
  global coins
  global coin_x
  global coin_y
  global player_x
  global player_y
  if player_y - 1 >= 0:
    field[player_x][player_y] = " "
    player_y -= 1
  if player_x == coin_x and player_y == coin_y:
    coins += 1

keyboard.add_hotkey("w", move_up)
keyboard.add_hotkey("s", move_down)
keyboard.add_hotkey("a", move_right)
keyboard.add_hotkey("d", move_left)

game()

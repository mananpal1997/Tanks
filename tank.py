import pygame, time, random

pygame.init()

disp_width = 1000
disp_height = 600

game_disp = pygame.display.set_mode((disp_width,disp_height))

fire_sound = pygame.mixer.Sound('C:/Python27/Lib/site-packages/pygame/examples/data/secosmic_lo.wav')
explosion_sound = pygame.mixer.Sound('C:/Python27/Lib/site-packages/pygame/examples/data/boom.wav')

pygame.display.set_caption('Tanks Game')

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)

clock = pygame.time.Clock()

tank_width = 40
tank_height = 20
tirret_width = 5
wheel_width = 5
ground_height = 35

font1 = pygame.font.SysFont("comicsansms", 25)
font2 = pygame.font.SysFont("comicsansms", 50)
font3 = pygame.font.SysFont("comicsansms", 85)

def score(score):
    text = font1.render("Score: "+str(score), True, black)
    game_disp.blit(text, [0,0])

def text_obj(text, color,size = "small"):

    if(size == "small"):
        text_surface = font1.render(text, True, color)
    if(size == "medium"):
        text_surface = font2.render(text, True, color)
    if(size == "large"):
        text_surface = font3.render(text, True, color)

    return text_surface, text_surface.get_rect()

def button_text(msg, color, b_x, b_y, b_w, b_h, size = "small"):
    text_surface, text_rect = text_obj(msg, color, size)
    text_rect.center = ((b_x+(b_w/2)), b_y+(b_h/2))
    game_disp.blit(text_surface, text_rect)
   
def flash_message(msg,color, y_displace = 0, size = "small"):
    text_surface, text_rect = text_obj(msg, color, size)
    text_rect.center = (int(disp_width / 2), int(disp_height / 2)+y_displace)
    game_disp.blit(text_surface, text_rect)

def tank(x,y,turret_pos):
    x = int(x)
    y = int(y)

    possible_turrets = [(x-27, y-2), (x-26, y-5), (x-25, y-8), (x-23, y-12), (x-20, y-14), (x-18, y-15), (x-15, y-17), (x-13, y-19), (x-11, y-21)]
  
    pygame.draw.circle(game_disp, black, (x,y), int(tank_height/2))
    pygame.draw.rect(game_disp, black, (x-tank_height, y, tank_width, tank_height))

    pygame.draw.line(game_disp, black, (x,y), possible_turrets[turret_pos], tirret_width)

    pygame.draw.circle(game_disp, black, (x-15, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x-10, y+20), wheel_width)
       
    pygame.draw.circle(game_disp, black, (x-15, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x-10, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x-5, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x+5, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x+10, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x+15, y+20), wheel_width)

    return possible_turrets[turret_pos]

def enemy_tank(x,y,turret_pos):
    x = int(x)
    y = int(y)

    possible_turrets = [(x+27, y-2), (x+26, y-5), (x+25, y-8), (x+23, y-12), (x+20, y-14), (x+18, y-15), (x+15, y-17), (x+13, y-19), (x+11, y-21)]
  
    pygame.draw.circle(game_disp, black, (x,y), int(tank_height/2))
    pygame.draw.rect(game_disp, black, (x-tank_height, y, tank_width, tank_height))

    pygame.draw.line(game_disp, black, (x,y), possible_turrets[turret_pos], tirret_width)

    pygame.draw.circle(game_disp, black, (x-15, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x-10, y+20), wheel_width)
       
    pygame.draw.circle(game_disp, black, (x-15, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x-10, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x-5, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x+5, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x+10, y+20), wheel_width)
    pygame.draw.circle(game_disp, black, (x+15, y+20), wheel_width)

    return possible_turrets[turret_pos]

def game_controls():
    game_control = True

    while(game_control):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

        game_disp.fill(white)
        flash_message("Controls", green, -100, size = "large")
        flash_message("Fire: Spacebar", black, -30)
        flash_message("Move Turret: Up-Down arrows", black, 10)
        flash_message("Move Tank: Left-Right arrows", black, 40)
        flash_message("Change Power: A(decrease)-D(increase)", black, 70)
        flash_message("Pause: P", black, 90)

        button("Play", 50, 500, 100, 50, green, light_green, action = "play")
        button("Main Menu", 450, 500, 100, 50, yellow, light_yellow, action = "main")
        button("Quit", 850, 500, 100, 50, red, light_red, action = "quit")

        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if(x + width > cur[0] > x and y + height > cur[1] > y):
        pygame.draw.rect(game_disp, active_color, (x, y, width, height))
        if(click[0] == 1 and action != None):
            if(action == "quit"):
                pygame.quit()
                quit()

            if(action == "controls"):
                game_controls()

            if(action == "play"):
                game_loop()

            if(action == "main"):
                start_game()            
    else:
        pygame.draw.rect(game_disp, inactive_color, (x,y,width,height))

    button_text(text, black, x, y, width, height)

def pause():
    paused = True

    flash_message("Paused",black,-100,size="large")
    flash_message("Press C to continue playing or Q to quit",black,25)
    pygame.display.update()

    while(paused):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_c):
                    paused = False
                elif(event.key == pygame.K_q):
                    pygame.quit()
                    quit()

        clock.tick(5)
        
def draw_barrier(xlocation, random_height, barrier_width):
    pygame.draw.rect(game_disp, black, [xlocation, disp_height - random_height, barrier_width, random_height])
    
def explosion(x, y, size=50):
    pygame.mixer.Sound.play(explosion_sound)
    explode = True

    while(explode):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

        colors = [red, light_red, yellow, light_yellow]
        magnitude = 1

        while(magnitude < size):
            explode_x = x +random.randrange(-1*magnitude, magnitude)
            explode_y = y +random.randrange(-1*magnitude, magnitude)

            pygame.draw.circle(game_disp, colors[random.randrange(0, 4)], (explode_x, explode_y), random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False

def fire_shell(xy, tank_x, tank_y, turret_pos, gun_power, xlocation, barrier_width, random_height, etank_x, etank_y):
    pygame.mixer.Sound.play(fire_sound)
    fire = True
    damage = 0

    staring_shell = list(xy)

    while(fire):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

        pygame.draw.circle(game_disp, red, (staring_shell[0], staring_shell[1]), 5)

        staring_shell[0] -= (12 - turret_pos)*2
        staring_shell[1] += int((((staring_shell[0] - xy[0])*0.015 / (gun_power/50.0))**2) - (turret_pos + turret_pos / (12 - turret_pos)))

        if(staring_shell[1] > disp_height-ground_height):
            hit_x = int((staring_shell[0]*disp_height - ground_height) / staring_shell[1])
            hit_y = int(disp_height - ground_height)
            
            if(etank_x + 10 > hit_x > etank_x - 10):
                #Critical Hit
                damage = 25
            elif(etank_x + 15 > hit_x > etank_x - 15):
                #Hard Hit
                damage = 20
            elif(etank_x + 20 > hit_x > etank_x - 20):
                #Medium Hit
                damage = 15
            elif(etank_x + 25 > hit_x > etank_x - 25):
                #Light Hit
                damage = 10
            
            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = staring_shell[0] <= xlocation + barrier_width
        check_x_2 = staring_shell[0] >= xlocation

        check_y_1 = staring_shell[1] <= disp_height
        check_y_2 = staring_shell[1] >= disp_height - random_height

        if(check_x_1 and check_x_2 and check_y_1 and check_y_2):
            hit_x = int(staring_shell[0])
            hit_y = int(staring_shell[1])

            explosion(hit_x, hit_y)
            fire = False
            
        pygame.display.update()
        clock.tick(60)

    return damage
        
def e_fire_shell(xy, tank_x, tank_y, turret_pos, gun_power, xlocation, barrier_width, random_height, ptank_x, ptank_y):
    pygame.mixer.Sound.play(fire_sound)
    damage = 0
    cur_power = 1
    power_found = False

    while(not power_found):
        cur_power += 1
        if(cur_power > 100):
            power_found = True
            break

        fire = True
        staring_shell = list(xy)

        while(fire):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    quit()

            staring_shell[0] += (12 - turret_pos)*2
            staring_shell[1] += int((((staring_shell[0] - xy[0])*0.015 / (cur_power/50.0))**2) - (turret_pos + turret_pos/(12 - turret_pos)))

            if(staring_shell[1] > disp_height-ground_height):
                hit_x = int((staring_shell[0]*disp_height - ground_height) / staring_shell[1])
                hit_y = int(disp_height - ground_height)
                if(ptank_x+15 > hit_x > ptank_x - 15):
                    #target acquired
                    power_found = True
                fire = False

            check_x_1 = staring_shell[0] <= xlocation + barrier_width
            check_x_2 = staring_shell[0] >= xlocation

            check_y_1 = staring_shell[1] <= disp_height
            check_y_2 = staring_shell[1] >= disp_height - random_height

            if(check_x_1 and check_x_2 and check_y_1 and check_y_2):
                hit_x = int(staring_shell[0])
                hit_y = int(staring_shell[1])
                fire = False
        
    fire = True
    staring_shell = list(xy)

    while(fire):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

        pygame.draw.circle(game_disp, red, (staring_shell[0], staring_shell[1]), 5)

        staring_shell[0] += (12 - turret_pos)*2
        gun_power = random.randrange(int(cur_power*0.90), int(cur_power*1.10))
        staring_shell[1] += int((((staring_shell[0] - xy[0])*0.015 / (gun_power/50.0))**2) - (turret_pos + turret_pos/(12 - turret_pos)))

        if(staring_shell[1] > disp_height - ground_height):
            hit_x = int((staring_shell[0]*disp_height - ground_height) / staring_shell[1])
            hit_y = int(disp_height - ground_height)

            if(ptank_x + 10 > hit_x > ptank_x - 10):
                #Critical Hit
                damage = 25
            elif(ptank_x + 15 > hit_x > ptank_x - 15):
                #Hard Hit
                damage = 20
            elif(ptank_x + 20 > hit_x > ptank_x - 20):
                #Medium Hit
                damage = 15
            elif(ptank_x + 25 > hit_x > ptank_x - 25):
                #Light Hit
                damage = 10
            
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = staring_shell[0] <= xlocation + barrier_width
        check_x_2 = staring_shell[0] >= xlocation

        check_y_1 = staring_shell[1] <= disp_height
        check_y_2 = staring_shell[1] >= disp_height - random_height

        if(check_x_1 and check_x_2 and check_y_1 and check_y_2):
            hit_x = int(staring_shell[0])
            hit_y = int(staring_shell[1])

            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)

    return damage

def power(level):
    text = font1.render("Power: "+str(level)+"%",True, black)
    game_disp.blit(text, [440,0])

def start_game():

    game_play = True

    while(game_play):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_c):
                    game_play = False
                elif(event.key == pygame.K_q):
                    pygame.quit()
                    quit()

        game_disp.fill(white)
        flash_message("Welcome to Tanks Game!", green, -100, size=  "large")

        button("Play", 50, 500, 100, 50, green, light_green, action = "play")
        button("Controls", 450, 500, 100, 50, yellow, light_yellow, action = "controls")
        button("Quit", 850, 500, 100, 50, red, light_red, action = "quit")

        pygame.display.update()
        clock.tick(15)

def game_over():
    gameover = True

    while(gameover):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

        game_disp.fill(white)
        flash_message("Game Over", green, -100, size = "large")

        button("Play Again", 50, 500, 150, 50, green, light_green, action = "play")
        button("Controls", 450, 500, 100, 50, yellow, light_yellow, action = "controls")
        button("Quit", 850, 500, 100, 50, red, light_red, action = "quit")

        pygame.display.update()
        clock.tick(15)

def winner():
    win = True

    while(win):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()

        game_disp.fill(white)
        flash_message("Congratulations, You won!", green, -100, size = "large")

        button("Play Again", 50, 500, 150, 50, green, light_green, action = "play")
        button("Controls", 450, 500, 100, 50, yellow, light_yellow, action = "controls")
        button("Quit", 850, 500, 100, 50, red, light_red, action = "quit")
        
        pygame.display.update()
        clock.tick(15)

def draw_health_bars(p_health, e_health):

    if(p_health > 75):
        p_health_color = green
    elif(p_health > 50):
        p_health_color = yellow
    else:
        p_health_color = red

    if(e_health > 75):
        e_health_color = green
    elif(e_health > 50):
        e_health_color = yellow
    else:
        e_health_color = red

    text_surf1, text_rect1 = text_obj("Player Health : "+str(p_health), black)
    text_surf2, text_rect2 = text_obj("Enemy Health : "+str(e_health), black)

    text_rect1.center = [870, 75]
    text_rect2.center = [130, 75]
    

    pygame.draw.rect(game_disp, p_health_color, (760, 25, p_health, 25))
    pygame.draw.rect(game_disp, e_health_color, (20, 25, e_health, 25))
    game_disp.blit(text_surf1, text_rect1)
    game_disp.blit(text_surf2, text_rect2)

def game_loop():
    game_exit = False
    gameover = False
    fps = 20

    p_health = 100
    e_health = 100

    ptank_x = disp_width * 0.9
    ptank_y = disp_height * 0.9
    tank_move = 0
    current_turret_pos = 0
    change_turret = 0
    etank_x = disp_width * 0.1
    etank_y = disp_height * 0.9
    
    fire_power = 50
    power_change = 0

    barrier_width = 50
    xlocation = (440) + random.randint(-0.2*disp_width, 0.2*disp_width) 
    random_height = random.randrange(disp_height*0.1,disp_height*0.6)

    while(not game_exit):
        if(gameover == True):
            flash_message("Game Over", red, -50, size = "large")
            flash_message("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while(gameover == True):
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        game_exit = True
                        gameover = False

                    if(event.type == pygame.KEYDOWN):
                        if(event.key == pygame.K_c):
                            game_loop()
                        elif(event.key == pygame.K_q):
                            game_exit = True
                            gameover = False
                            
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                game_exit = True

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    tank_move = -5
                elif(event.key == pygame.K_RIGHT):
                    tank_move = 5
                elif(event.key == pygame.K_UP):
                    change_turret = 1
                elif(event.key == pygame.K_DOWN):
                    change_turret = -1
                elif(event.key == pygame.K_p):
                    pause()
                elif(event.key == pygame.K_SPACE):
                    damage = fire_shell(gun, ptank_x, ptank_y, current_turret_pos, fire_power, xlocation, barrier_width, random_height, etank_x, etank_y)
                    e_health -= damage

                    if(p_health < 1):
                        game_over()
                    elif(e_health < 1):
                        winner()

                    possible_movement = ['f', 'r']
                    move = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):
                        if(disp_width*0.3 > etank_x > disp_width*0.03):
                            if(possible_movement[move] == "f"):
                                etank_x += 5
                            elif(possible_movement[move] == "r"):
                                etank_x -= 5
                            if(etank_x > xlocation - etank_x):
                                etank_x -= 5
                            if(etank_x <= 0):
                                etank_x += 5

                            game_disp.fill(white)
                            draw_health_bars(p_health, e_health)
                            gun = tank(ptank_x, ptank_y, current_turret_pos)
                            enemy_gun = enemy_tank(etank_x, etank_y, 8)

                            fire_power += power_change
                            power(fire_power)

                            draw_barrier(xlocation, random_height, barrier_width)
                            game_disp.fill(green, rect=[0, disp_height - ground_height, disp_width, ground_height])
                            pygame.display.update()
                            clock.tick(fps)

                    damage = e_fire_shell(enemy_gun, etank_x, etank_y, 8, 50, xlocation, barrier_width, random_height, ptank_x, ptank_y)
                    p_health -= damage
                    
                elif(event.key == pygame.K_a):
                    power_change = -1
                elif(event.key == pygame.K_d):
                    power_change = 1

            elif(event.type == pygame.KEYUP):
                if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    tank_move = 0
                if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    change_turret = 0
                if(event.key == pygame.K_a or event.key == pygame.K_d):
                    power_change = 0

        ptank_x += tank_move
        if(ptank_x > disp_width - 20):
            ptank_x = disp_width - 20
        current_turret_pos += change_turret

        if(current_turret_pos > 8):
            current_turret_pos = 8
        elif(current_turret_pos < 0):
            current_turret_pos = 0

        if(ptank_x - (tank_width/2) < xlocation + barrier_width):
            ptank_x += 5
            
        game_disp.fill(white)
        draw_health_bars(p_health, e_health)
        gun = tank(ptank_x, ptank_y, current_turret_pos)
        enemy_gun = enemy_tank(etank_x, etank_y, 8)

        if(p_health < 1):
            game_over()
        elif(e_health < 1):
            winner()

        if(fire_power < 100 and fire_power > 1):
            fire_power += power_change
        elif(fire_power == 100 and power_change == -1):
            fire_power += power_change
        elif(fire_power == 1 and power_change == 1):
            fire_power += power_change
        power(fire_power)

        draw_barrier(xlocation, random_height, barrier_width)
        game_disp.fill(green, rect=[0, disp_height - ground_height, disp_width, ground_height])
        pygame.display.update()

        if(p_health < 1):
            game_over()
        elif(e_health < 1):
            winner()
        clock.tick(fps)

    pygame.quit()
    quit()

start_game()
game_loop()

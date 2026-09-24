import pygame
import random

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FP")
clock = pygame.time.Clock()

#player
player_img = pygame.image.load("FP/assets/player.png").convert_alpha()
player_width = player_img.get_width()*0.05
player_height = player_img.get_height()*0.05
player_img = pygame.transform.scale(player_img,(player_width, player_height))
player_speed = 5
player_x = WIDTH//2 - player_width//2
player_y = HEIGHT//2 - player_height//2

#gato
idle_img = pygame.image.load("FP/assets/idle.png").convert_alpha()
happy_img = pygame.image.load("FP/assets/hapi.png").convert_alpha()
angry_img = pygame.image.load("FP/assets/mayah.png").convert_alpha()
cat_width = idle_img.get_width()*0.1
cat_height = idle_img.get_height()*0.1
idle_img = pygame.transform.scale(idle_img,(cat_width, cat_height))
happy_img = pygame.transform.scale(happy_img,(cat_width, cat_height))
angry_img = pygame.transform.scale(angry_img,(cat_width, cat_height))
cat_x = WIDTH//4 - cat_width//2
cat_y = HEIGHT//4 - cat_height//2

#ingredients
rice_img = pygame.image.load("FP/assets/putih.png").convert_alpha()
meat_img = pygame.image.load("FP/assets/abang.png").convert_alpha()
vegs_img = pygame.image.load("FP/assets/ijo.png").convert_alpha()
tempe_img = pygame.image.load("FP/assets/oren.png").convert_alpha()
ing_width = rice_img.get_width()*0.1
ing_height = rice_img.get_height()*0.1
rice_img = pygame.transform.scale(rice_img,(ing_width, ing_height))
meat_img = pygame.transform.scale(meat_img,(ing_width, ing_height))
vegs_img = pygame.transform.scale(vegs_img,(ing_width, ing_height))
tempe_img = pygame.transform.scale(tempe_img,(ing_width, ing_height))
ing_x1 = WIDTH - ((WIDTH//4)*4)
ing_x2 = WIDTH - ((WIDTH//4)*3)
ing_x3 = WIDTH - ((WIDTH//4)*2)
ing_x4 = WIDTH - ((WIDTH//4))
ing_y1 = HEIGHT - HEIGHT//4
ing_y2 = HEIGHT - HEIGHT//4
ing_y3 = HEIGHT - HEIGHT//4
ing_y4 = HEIGHT - HEIGHT//4

#state ingredients
start_x1, start_y1 = ing_x1, ing_y1
start_x2, start_y2 = ing_x2, ing_y2
start_x3, start_y3 = ing_x3, ing_y3
start_x4, start_y4 = ing_x4, ing_y4

#food
fullmeal_img = pygame.image.load("FP/assets/full meal.png").convert_alpha()
noR_img = pygame.image.load("FP/assets/ijoabangoren.png").convert_alpha()
noM_img = pygame.image.load("FP/assets/ijoputihoren.png").convert_alpha()
noV_img = pygame.image.load("FP/assets/abangputihoren.png").convert_alpha()
noT_img = pygame.image.load("FP/assets/ijoputihabang.png").convert_alpha()
rt_img = pygame.image.load("FP/assets/putihoren.png").convert_alpha()
rm_img = pygame.image.load("FP/assets/putihabang.png").convert_alpha()
rv_img = pygame.image.load("FP/assets/ijoputih.png").convert_alpha()
mv_img = pygame.image.load("FP/assets/ijoabang.png").convert_alpha()
mt_img = pygame.image.load("FP/assets/orenabang.png").convert_alpha()
vt_img = pygame.image.load("FP/assets/ijoren.png").convert_alpha()
meal_width = fullmeal_img.get_width()*0.1
meal_height = fullmeal_img.get_height()*0.1
fullmeal_img = pygame.transform.scale(fullmeal_img,(meal_width, meal_height))
noR_img = pygame.transform.scale(noR_img,(meal_width, meal_height))
noM_img = pygame.transform.scale(noM_img,(meal_width, meal_height))
noV_img = pygame.transform.scale(noV_img,(meal_width, meal_height))
noT_img = pygame.transform.scale(noT_img,(meal_width, meal_height))
rt_img = pygame.transform.scale(rt_img,(meal_width, meal_height))
rm_img = pygame.transform.scale(rm_img,(meal_width, meal_height))
rv_img = pygame.transform.scale(rv_img,(meal_width, meal_height))
mv_img = pygame.transform.scale(mv_img,(meal_width, meal_height))
mt_img = pygame.transform.scale(mt_img,(meal_width, meal_height))
vt_img = pygame.transform.scale(vt_img,(meal_width, meal_height))

all_foods = [fullmeal_img, noR_img, noM_img, noV_img, noT_img, rt_img, rm_img, rv_img, mv_img, mt_img, vt_img]

#state awal gato
cat_state = "waiting"
cat_requested_food = None
cat_timer = 0
#gato req
next_request_time = pygame.time.get_ticks() + random.randint(2000, 10000) 
happy_angry_timer = 0

#state awal
has_rice = False
has_meat = False
has_vegs = False
has_tempe = False
carried_food = None
score = 0

stove_rect = pygame.Rect(700, 150, 50, 50)
score_font = pygame.font.SysFont("Arial", 40, bold=True)

running = True
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #player keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            player_x -= player_speed
    if keys[pygame.K_RIGHT]:
            player_x += player_speed
    if keys[pygame.K_UP]:
            player_y -= player_speed
    if keys[pygame.K_DOWN]:
            player_y += player_speed

    #batas gerak player
    player_x = max(0, min(player_x, WIDTH-player_width))
    player_y = max(0, min(player_y, HEIGHT-player_height))

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    cat_rect = pygame.Rect(cat_x, cat_y, cat_width, cat_height) 

    #take ingredients
    if not has_rice:
        r_rect = pygame.Rect(ing_x1, ing_y1, ing_width, ing_height)
        if player_rect.colliderect(r_rect):
            has_rice = True
    if not has_meat:
        m_rect = pygame.Rect(ing_x2, ing_y2, ing_width, ing_height)
        if player_rect.colliderect(m_rect):
            has_meat = True
    if not has_vegs:
        v_rect = pygame.Rect(ing_x3, ing_y3, ing_width, ing_height)
        if player_rect.colliderect(v_rect):
            has_vegs = True
    if not has_tempe:
        t_rect = pygame.Rect(ing_x4, ing_y4, ing_width, ing_height)
        if player_rect.colliderect(t_rect):
            has_tempe = True

    #COOK(ed)
    if player_rect.colliderect(stove_rect) and carried_food is None:
        cooked_something = False

        if has_rice and has_meat and has_vegs and has_tempe:
            carried_food = fullmeal_img
            has_rice = has_meat = has_vegs = has_tempe = False
            cooked_something = True
        elif not has_rice and has_meat and has_vegs and has_tempe:
            carried_food = noR_img
            has_meat = has_vegs = has_tempe = False
            cooked_something = True
        elif has_rice and not has_meat and has_vegs and has_tempe:
            carried_food = noM_img
            has_rice = has_vegs = has_tempe = False
            cooked_something = True
        elif has_rice and has_meat and not has_vegs and has_tempe:
            carried_food = noV_img
            has_rice = has_meat = has_tempe = False
            cooked_something = True
        elif has_rice and has_meat and has_vegs and not has_tempe:
            carried_food = noT_img
            has_rice = has_meat = has_vegs = False
            cooked_something = True
        elif has_rice and has_tempe and not has_meat and not has_vegs:
            carried_food = rt_img
            has_rice = has_tempe = False
            cooked_something = True
        elif has_rice and has_meat and not has_vegs and not has_tempe:
            carried_food = rm_img
            has_rice = has_meat = False
            cooked_something = True
        elif has_rice and has_vegs and not has_meat and not has_tempe:
            carried_food = rv_img
            has_rice = has_vegs = False
            cooked_something = True
        elif has_meat and has_vegs and not has_rice and not has_tempe:
            carried_food = mv_img
            has_meat = has_vegs = False
            cooked_something = True
        elif has_meat and has_tempe and not has_rice and not has_vegs:
            carried_food = mt_img
            has_meat = has_tempe = False
            cooked_something = True
        elif has_vegs and has_tempe and not has_rice and not has_meat:
            carried_food = vt_img
            has_vegs = has_tempe = False
            cooked_something = True
        #reset ingredients
        if cooked_something:
            ing_x1, ing_y1 = start_x1, start_y1
            ing_x2, ing_y2 = start_x2, start_y2
            ing_x3, ing_y3 = start_x3, start_y3
            ing_x4, ing_y4 = start_x4, start_y4

    #cat request
    if cat_state == "waiting":
        if current_time >= next_request_time:
            cat_state = "requesting"
            cat_requested_food = random.choice(all_foods)
            cat_timer = current_time + 10000
            
    elif cat_state == "requesting":
        if current_time >= cat_timer:
            cat_state = "angry"
            happy_angry_timer = current_time + 3000
            cat_requested_food = None

            ing_x1, ing_y1 = start_x1, start_y1
            ing_x2, ing_y2 = start_x2, start_y2
            ing_x3, ing_y3 = start_x3, start_y3
            ing_x4, ing_y4 = start_x4, start_y4

            has_rice = has_meat = has_vegs = has_tempe = False
            carried_food = None

        elif player_rect.colliderect(cat_rect) and carried_food is not None:
            if carried_food == cat_requested_food:
                cat_state = "happy"
                happy_angry_timer = current_time + 2000
                carried_food = None
                cat_requested_food = None
                score += 1
            else:
                cat_state = "angry"
                happy_angry_timer = current_time + 3000
                cat_requested_food = None
                
                ing_x1, ing_y1 = start_x1, start_y1
                ing_x2, ing_y2 = start_x2, start_y2
                ing_x3, ing_y3 = start_x3, start_y3
                ing_x4, ing_y4 = start_x4, start_y4
                
                has_rice = has_meat = has_vegs = has_tempe = False
                carried_food = None
                
    elif cat_state == "happy" or cat_state == "angry":
        if current_time >= happy_angry_timer:
            cat_state = "waiting"
            next_request_time = current_time + random.randint(2000, 10000)

    screen.fill((203, 236, 145))
    score_surface = score_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

    #stove
    pygame.draw.rect(screen, (70, 49, 16), stove_rect)

    #draw a gato
    if cat_state == "happy":
        screen.blit(happy_img, (cat_x, cat_y))
    elif cat_state == "angry":
        screen.blit(angry_img, (cat_x, cat_y))
    else:
        screen.blit(idle_img, (cat_x, cat_y))

    #draw makanan gato
    if cat_state == "requesting" and cat_requested_food is not None:
        bubble_rect = pygame.Rect(cat_x + cat_width//2 - 20, cat_y - 60, 40, 40)
        # pygame.draw.rect(screen, (255, 255, 255), bubble_rect)
        # pygame.draw.rect(screen, (0, 0, 0), bubble_rect, 2)
        screen.blit(cat_requested_food, (bubble_rect.x + 5, bubble_rect.y + 5))
        
        time_left = cat_timer - current_time
        if time_left > 0:
            bar_width = (time_left / 10000) * 40
            pygame.draw.rect(screen, (255, 0, 0), (bubble_rect.x, bubble_rect.y + 45, bar_width, 5))

    #kalau sudah diambil
    if not has_rice: screen.blit(rice_img,(ing_x1,ing_y1))
    if not has_meat: screen.blit(meat_img,(ing_x2,ing_y2))
    if not has_vegs: screen.blit(vegs_img,(ing_x3,ing_y3))
    if not has_tempe: screen.blit(tempe_img,(ing_x4,ing_y4))

    screen.blit(player_img,(player_x,player_y))

    #kalau belum diambil
    if has_rice: screen.blit(rice_img, (player_x, player_y - ing_height))
    if has_meat: screen.blit(meat_img, (player_x, player_y - ing_height))
    if has_vegs: screen.blit(vegs_img, (player_x, player_y - ing_height))
    if has_tempe: screen.blit(tempe_img, (player_x, player_y - ing_height))

    if carried_food is not None:
        screen.blit(carried_food, (player_x, player_y - meal_height))

    pygame.display.update()
    clock.tick(60)        
pygame.quit()
define dark = Character("Darkness")

init:
    image bg minigame = Frame("minigame_assets/bg minigame.png",  40, 40, 40, 40, tile=True)


init python:
    import random
    import pygame
    import math

    object_borders = []

    def check_collision(x, y):
        for ob in object_borders: #(x0, y0, x1, y1) tuple
            if ((x >= ob[0] and x<= ob[2])) and (y >= ob[1] and y<= ob[3]):
                return True
        return False


    class PlayableSprite(renpy.Displayable):
        def __init__(self, chara_type, xpos, ypos, **properties):
            super(PlayableSprite, self).__init__(**properties)
            self.chara_type = chara_type
            if(self.chara_type == "companion"):
                self.img = "minigame_assets/companion.png"
                self.up_key = pygame.locals.K_UP
                self.left_key = pygame.locals.K_LEFT
                self.down_key = pygame.locals.K_DOWN
                self.right_key = pygame.locals.K_RIGHT
                self.flash_key = pygame.locals.K_q
            else:
                self.img ="minigame_assets/main_character.png"
                self.up_key = pygame.locals.K_w
                self.left_key = pygame.locals.K_a
                self.down_key =pygame.locals.K_s
                self.right_key = pygame.locals.K_d
                self.flash_key = pygame.locals.K_e


            self.sprite = Transform(self.img)

            self.xpos = xpos
            self.ypos = ypos

            self.is_flashing = False

            self.render_size = (1920, 1080)
                
        def attach_observer(self, observer):
            self.observer = observer
        
        def render(self, width, height, st, at):
            sprite_render = renpy.render(self.sprite, width, height, st, at)
            return sprite_render

        
        def event(self, ev, x, y, st):
            if (ev.key in [self.right_key, self.left_key, self.up_key, self.down_key]):
                self.observer.notify_obs("sound", self.xpos, self.ypos)

            if(ev.key == self.right_key):
                self.xpos += 10 if (not check_collision(self.xpos + 10, self.ypos)) else 0
            elif(ev.key == self.left_key):
                self.xpos -= 10 if (not check_collision(self.xpos - 10, self.ypos)) else 0
            elif(ev.key == self.up_key):
                self.ypos -= 10 if (not check_collision(self.xpos, self.ypos - 10)) else 0
            elif(ev.key == self.down_key):
                self.ypos += 10 if (not check_collision(self.xpos, self.ypos + 10)) else 0
            elif(ev.key == self.flash_key):
                self.is_flashing = not self.is_flashing
                self.change_sprite_state(self.is_flashing)
            
            if (self.is_flashing):
                self.observer.notify_obs("light", self.xpos, self.ypos)
            
        
        def change_sprite_state(self, flash):
            if (flash):
                self.sprite = Composite((256, 256), (150, 0), "minigame_assets/flashlight_aura.png", (0, 0), self.img)
            else:
                self.sprite = Transform(self.img)




            


    class GuardSprite(renpy.Displayable):
        def __init__(self, **properties):
            super(GuardSprite, self).__init__(**properties)
            self.xpos = 500
            self.ypos = 200
            self.xdir =  None
            self.ydir = None

            self.state = "idle" #idle, alert, static
            self.playable_list = []
            self.investigation_speed = 3

            self.sprite = Transform("minigame_assets/guard.png")

            self.render_size = (80, 80)
            self.game_over = False

        # Flashlight trigger   
        def vision_cone(self, x, y):
            return x in range(self.xpos - 500, self.xpos + 500) and y in range(self.ypos - 500, self.ypos + 500)
        
        # Step sounds trigger
        def sound_cone(self, x, y):
            return x in range(self.xpos - 200, self.xpos + 200) and y in range(self.ypos - 200, self.ypos + 200)
        
        # Catching
        def catch_cone(self, x, y):
            return x in range(self.xpos - 100, self.xpos + 100) and y in range(self.ypos - 100, self.ypos + 100)
        
        def move(self):
            if self.state == "static":
                pass
            elif self.state == "idle":
                m = self.random_move()
                self.xpos += m[0]
                self.ypos += m[1]
            else:
                self.xdir = 1 if(self.trigger_posx > self.xpos) else -1
                self.ydir = 1 if (self.trigger_posy > self.ypos) else -1

                if (self.xpos == self.trigger_posx and self.ypos == self.trigger_posy):
                    self.state = "idle"
                    self.trigger_posx = None
                    self.trigger_posy = None
                
                if(self.xpos != self.trigger_posx and not check_collision(self.xpos + (self.xdir * self.investigation_speed), self.ypos)):
                    self.xpos += self.xdir * self.investigation_speed

                if (self.ypos != self.trigger_posy and not check_collision(self.xpos, self.ypos + (self.ydir * self.investigation_speed))):
                    self.ypos += self.ydir * self.investigation_speed
                


                
        def random_move(self):
            return random.choice([-1, 0, 1]), random.choice([-1, 0, 1])

        def observe(self, playable):
            self.playable_list.append(playable)
            playable.attach_observer(self)
        
        def notify_obs(self, n_type , x, y):
            if((self.catch_cone(x, y))):
                self.game_over = True
                renpy.timeout(0)


            if ((n_type == "light" and self.vision_cone(x, y)) or ((n_type == "sound" and self.sound_cone(x, y)))):
                self.state = "alert"
                self.trigger_posx = x
                self.trigger_posy = y
            

        def render(self, width, height, st, at):
            self.move()
            sprite_render = renpy.render(self.sprite, width, height, st, at)
            return sprite_render

        
        def event(self, ev, x, y, st):
            pass


    class StealthGame(renpy.Displayable):
        def __init__(self, **properties):
            super(StealthGame, self).__init__(**properties)
            self.object_height = 20
            self.object_width = 20
            self.render_size = (1920, 1080)

            # Setting up coordinates of objects and sprites
            self.finish_x = 1600
            self.finish_y = 540

            self.object_reset()
            self.object_sprites = []
            for x in self.object_locations:
                # self.object_sprites.append(Image(x[0], xsize= self.object_width, ysize = self.object_height))
                self.object_sprites.append(Composite((256, 256), (0, 0), x[0], (0, 0), "minigame_assets/destination.png"))
            
            self.guard = GuardSprite()
            self.mc = PlayableSprite("main", 500, 50)
            self.companion = PlayableSprite("companion", 20, 80)
            self.finish_line = Image("minigame_assets/destination.png")

            self.guard.observe(self.mc)
            self.guard.observe(self.companion)

                
        
        
        def render(self, width, height, st, at):
            r = renpy.Render(self.render_size[0], self.render_size[1])
            
            for i in object_borders:
                tmp = renpy.render(Solid("#f00", xsize= 100, ysize=100), 100, 100, st, at)
                r.blit(tmp, (i[0], i[1]))
            
            for x in range(len(self.object_sprites)):
                o_loc = self.object_locations[x]
                o_sprite = self.object_sprites[x]
                pi = renpy.render(o_sprite, 20, 20, st, at)
                r.blit(pi, (o_loc[1], o_loc[2]))
                

            
            #Trigger rending for the sprites
            x = renpy.render(self.finish_line, width, height, st, at)
            r.blit(x, (self.finish_x, self.finish_y))


            x = self.guard.render(width, height, st, at)
            r.blit(x, (self.guard.xpos, self.guard.ypos))

            x = self.mc.render(width, height, st, at)
            r.blit(x, (self.mc.xpos, self.mc.ypos))

            x = self.companion.render(width, height, st, at)
            r.blit(x, (self.companion.xpos, self.companion.ypos))

            renpy.redraw(self, 0)

            if abs(self.guard.xpos - self.finish_x) < 250 and abs(self.guard.ypos - self.finish_y) <250:
                renpy.timeout(0)

            return r

        
        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                self.mc.event(ev, x, y, st)
                self.companion.event(ev, x, y, st)
            
            if self.guard.game_over:
                return "you lost"

            if abs(self.guard.xpos - self.finish_x) < 250 and abs(self.guard.ypos - self.finish_y) <250:
                return "you won"
            

        
        def visit(self):
            child_list = self.object_sprites
            return child_list
        
        # Need some proper level design for this thing because random sucks
        def object_reset(self):
            object_img = ["minigame_assets/plant.png", "minigame_assets/trashcan.png", "minigame_assets/sofa.png", "minigame_assets/vending_machine.png"]
            self.object_locations = []
            xpositions = list(range(10, self.render_size[0] - 200 , 50))
            ypositions = list(range(10, self.render_size[1] - 200, 50))


            while len(self.object_locations) < 15:
                new_space =  (random.choice(xpositions), random.choice(ypositions))
                xpositions.remove(new_space[0])
                ypositions.remove(new_space[1])
                self.object_locations.append((random.choice(object_img), new_space[0], new_space[1]))
                object_borders.append((new_space[0] - 70, new_space[1] - 200, new_space[0] + 70, new_space[1]))


label minigame():

    dark "Hello"
    window hide 
    $ quick_menu = False

    call screen stealth_minigame
    
    $ quick_menu = True
    window show

    if _return == "you lost":
        dark "Game Over"
    elif _return == "you won":
        dark "Yay!"

    return 

screen stealth_minigame():
    add "bg minigame"
    default s_game = StealthGame()
    add s_game

    text _("Yes")
    




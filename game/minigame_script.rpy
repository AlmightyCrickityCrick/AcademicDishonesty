define dark = Character("Darkness")

init:
    image bg minigame = Frame("minigame_assets/bg minigame.png",  40, 40, 40, 40, tile=True)
    image bg minigame tutorial = Image("minigame_assets/game_tutorial-transformed.png")
    image bg minigame detail = Image("minigame_assets/minigame_decoration.png")
    image bg tutorial = Image("minigame_assets/tutorial.png")
    image bg end = Solid("#000", xsize=1200, ysize =500)




init python:
    import random
    import pygame
    import math

    object_borders = []
    global_battery_nr = 0

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
                self.observer.notify_obs("sound", self.chara_type, self.xpos, self.ypos)

            if(ev.key == self.right_key):
                self.xpos += 10 if (not check_collision(self.xpos + 10, self.ypos)) else 0
            elif(ev.key == self.left_key):
                self.xpos -= 10 if (self.xpos-10 >= 0 and not check_collision(self.xpos - 10, self.ypos)) else 0
            elif(ev.key == self.up_key):
                self.ypos -= 10 if (self.ypos-10 >= 120 and not check_collision(self.xpos, self.ypos - 10)) else 0
            elif(ev.key == self.down_key):
                self.ypos += 10 if (not check_collision(self.xpos, self.ypos + 10)) else 0
            elif(ev.key == self.flash_key):
                if(self.is_flashing == False):
                    if globals() ['global_battery_nr'] > 0:
                        self.is_flashing = not self.is_flashing
                        self.change_sprite_state(self.is_flashing)
                else:
                    self.is_flashing = not self.is_flashing
                    self.change_sprite_state(self.is_flashing)
            
            if (self.is_flashing):
                self.observer.notify_obs("light", self.chara_type, self.xpos, self.ypos)
            
        
        def change_sprite_state(self, flash):
            if (flash):
                self.sprite = Composite((256, 256), (150, 0), "minigame_assets/flashlight_aura.png", (0, 0), self.img)
                globals() ['global_battery_nr'] -=1
            else:
                self.sprite = Transform(self.img)




            


    class GuardSprite(renpy.Displayable):
        def __init__(self, **properties):
            super(GuardSprite, self).__init__(**properties)
            self.xpos = 500
            self.ypos = 200
            self.xdir =  None
            self.ydir = None

            self.state = "static" #idle, alert, static
            self.playable_dict = {}
            self.investigation_speed = 3
            self.following_character = None


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
                self.ydir = random.choice([1, -1])
                self.xdir = random.choice([1, -1])
                self.state = "idle"
            elif self.state == "idle":
                m = self.random_move()
                if(self.xpos + m[0] * self.xdir > 100 and self.xpos + m[0] * self.xdir < 1800 and not check_collision(self.xpos + m[0] * self.xdir, self.ypos)):
                    self.xpos += m[0] * self.xdir 
                else:
                    self.state = "static"

                if(self.ypos + m[1] * self.ydir > 120 and self.ypos + m[1] * self.ydir < 700 and not check_collision(self.xpos, self.ypos + m[1] * self.ydir)):
                    self.ypos += m[1] * self.ydir 
                else:
                    self.state = "static"
            else:
                self.xdir = 1 if(self.trigger_posx > self.xpos) else -1
                self.ydir = 1 if (self.trigger_posy > self.ypos) else -1

                if (self.xpos == self.trigger_posx and self.ypos == self.trigger_posy):
                    self.notify_obs("", self.following_character, self.playable_dict[self.following_character].xpos, self.playable_dict[self.following_character].ypos)
                    self.state = "idle"
                    self.trigger_posx = None
                    self.trigger_posy = None
                
                self.try_go_vertical()
                self.try_go_horizontal()

        #Define straight movement with obstacle collision clause        
        def try_go_vertical(self):
            if(self.xpos != self.trigger_posx):
                if not check_collision(self.xpos + (self.xdir * self.investigation_speed), self.ypos):
                    self.xpos += self.xdir * self.investigation_speed

        
        def try_go_horizontal(self):
            if (self.ypos != self.trigger_posy):
                if not check_collision(self.xpos, self.ypos + (self.ydir * self.investigation_speed)):
                    self.ypos += self.ydir * self.investigation_speed
                
        def random_move(self):
            return random.choice([0, 1, 2, 3]), random.choice([0, 1, 2, 3])

        def observe(self, playable):
            self.playable_dict[playable.chara_type] = playable
            playable.attach_observer(self)
        
        def notify_obs(self, n_type, c_type, x, y):
            if((self.catch_cone(x, y))):
                self.game_over = True
                renpy.timeout(0)


            if ((n_type == "light" and self.vision_cone(x, y)) or ((n_type == "sound" and self.sound_cone(x, y)))):
                self.state = "alert"
                self.trigger_posx = x
                self.trigger_posy = y
                self.following_character = c_type
            

        def render(self, width, height, st, at):
            self.move()
            sprite_render = renpy.render(self.sprite, width, height, st, at)
            return sprite_render

        
        def event(self, ev, x, y, st):
            pass


    class StealthGame(renpy.Displayable):
        def __init__(self, coin_nr, battery_nr, **properties):
            super(StealthGame, self).__init__(**properties)
            #Game Size saved as variable
            self.render_size = (1920, 1080)

            #Upper Menu Objects
            self.coin_nr = coin_nr
            globals() ['global_battery_nr'] = battery_nr
            self.stars_found = 0
            self.menu = Image("minigame_assets/top_bar.png")
            self.small_star_sprite = Image("minigame_assets/small_star.png")
            self.coin_sprite = Image("minigame_assets/coin.png")
            self.eye_sprite = Image("minigame_assets/white_eye.png")


            # Setting up coordinates of where the guard has to be moved to finish the game (blue square)
            self.finish_x = 1600
            self.finish_y = 540

            # Setting up the positions of objects and stars
            self.object_reset()

            # Defining the game object sprites
            self.object_sprites = []
            for x in self.object_locations:
                self.object_sprites.append(Image(x[0]))
            
            self.guard = GuardSprite()
            self.mc = PlayableSprite("main", 500, 200)
            self.companion = PlayableSprite("companion", 20, 700)
            self.finish_line = Image("minigame_assets/destination.png")
            self.star_sprite = Image("minigame_assets/star.png")
            self.battery_sprite = Image("minigame_assets/battery.png")

            self.guard.observe(self.mc)
            self.guard.observe(self.companion)

                
        def render_menu(self, r, width, height, st, at):
            #Renders top bar
            x = renpy.render(self.menu, width, height, st, at)
            r.blit(x, (350, -50))
            #Renders Battery
            x = renpy.render(self.battery_sprite, width, height, st, at)
            r.blit(x, (600, 62))

            #Renders Battery Nr
            x = renpy.render(Text(str(global_battery_nr), size=26, color="#c23535"), width, height, st, at)
            r.blit(x, (630, 67))

            #Renders coin
            x = renpy.render(self.coin_sprite, width, height, st, at)
            r.blit(x, (670, 62))
            
            #Renders Coin Nr
            x = renpy.render(Text(str(self.coin_nr), size=26, color="#c23535"), width, height, st, at)
            r.blit(x, (710, 67))

            self.setup_eye(r, width, height, st, at)
            
            #Renders Coin Nr
            x = renpy.render(Text(str(self.coin_nr), size=26, color="#c23535"), width, height, st, at)
            r.blit(x, (710, 67))

            #Renders Stars on Top Bar
            for i in range(self.stars_found):
                x = renpy.render(self.small_star_sprite, width, height, st, at)
                r.blit(x, (1200 + 50 * i, 62))

        def setup_eye(self, r, width, height, st, at):
            if (self.guard.catch_cone(self.mc.xpos, self.mc.ypos) or self.guard.catch_cone(self.companion.xpos, self.companion.ypos)):
                self.eye_sprite =  Image("minigame_assets/red_eye.png")
            elif(self.guard.sound_cone(self.mc.xpos, self.mc.ypos) or self.guard.sound_cone(self.companion.xpos, self.companion.ypos)):
                self.eye_sprite = Image("minigame_assets/yellow_eye.png")
            else:
                self.eye_sprite = Image("minigame_assets/white_eye.png")

            #Renders eye
            x = renpy.render(self.eye_sprite, width, height, st, at)
            r.blit(x, (920, 65))
        
        def render_game_zone(self, r, width, height, st, at):
            # Render of stars in game zone
            for i in self.star_locations.values():
                pi = renpy.render(self.star_sprite, 40, 40, st, at)
                r.blit(pi, (i[1], i[2]))
            
            # Render of Game objects
            for x in range(len(self.object_sprites)):
                o_loc = self.object_locations[x]
                o_sprite = self.object_sprites[x]
                pi = renpy.render(o_sprite, 20, 20, st, at)
                r.blit(pi, (o_loc[1], o_loc[2]))
                
            #Trigger rending for the sprites:
            #Finish Line - Blue square
            if (self.stars_found >0):
                x = renpy.render(self.finish_line, width, height, st, at)
                r.blit(x, (self.finish_x, self.finish_y))

            #Guard
            x = self.guard.render(self.render_size[0], self.render_size[1], st, at)
            r.blit(x, (self.guard.xpos, self.guard.ypos))

            #MC
            x = self.mc.render(width, height, st, at)
            r.blit(x, (self.mc.xpos, self.mc.ypos))

            #Companion
            x = self.companion.render(self.render_size[0], self.render_size[1], st, at)
            r.blit(x, (self.companion.xpos, self.companion.ypos))

        
        def render(self, width, height, st, at):
            r = renpy.Render(self.render_size[0], self.render_size[1])
            
            self.render_menu(r, width, height, st, at)
            self.render_game_zone(r, width, height, st, at)

            renpy.redraw(self, 0)

            # Checks each render if the guard is at the finishing lane
            if abs(self.guard.xpos - self.finish_x) < 100 and abs(self.guard.ypos + 150 - self.finish_y) < 250:
                renpy.timeout(0)

            return r

        
        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                self.mc.event(ev, x, y, st)
                self.companion.event(ev, x, y, st)
            
            self.check_star_collected()

            if self.guard.game_over:
                if self.coin_nr > 0:
                    self.guard.game_over = False
                    self.coin_nr -= 1
                else:
                    return "lost"

            if abs(self.guard.xpos - self.finish_x) < 100 and abs(self.guard.ypos - self.finish_y) <250 and self.stars_found > 1:
                return "won"


        #Checks if MC or Companion position coincides wih a star
        def check_star_collected(self):
            to_be_deleted = None
            for s in self.star_locations.values():
                if (abs(self.mc.xpos - s[1]) < 150 and abs((self.mc.ypos + 100)- s[2]) < 50) or (abs(self.companion.xpos - s[1]) < 150 and abs((self.companion.ypos + 100)  - s[2]) < 50):
                    to_be_deleted = s
                    break
            # Deletes the star from the dictionary of stars to be rendered and adds it to be rendered in top bar
            if to_be_deleted:
                self.star_locations.pop((to_be_deleted[1], to_be_deleted[2]))
                self.stars_found += 1

        def visit(self):
            child_list = self.object_sprites
            return child_list
        
        #TODO: Need some proper level design for this thing because random sucks
        def object_reset(self):
            object_img = ["minigame_assets/plant.png", "minigame_assets/trashcan.png", "minigame_assets/sofa.png", "minigame_assets/vending_machine.png"]
            self.object_locations = []
            xpositions = list(range(70, self.render_size[0] - 200 , 50))
            ypositions = list(range(200, self.render_size[1] - 200, 50))
            globals() ['object_borders'] = []

            #Sets objects around the room
            while len(self.object_locations) < 10:
                new_space =  (random.choice(xpositions), random.choice(ypositions))
                xpositions.remove(new_space[0])
                ypositions.remove(new_space[1])
                self.object_locations.append((random.choice(object_img), new_space[0], new_space[1]))
                #Adds the current object's borders to a list
                object_borders.append((new_space[0] - 70, new_space[1] - 200, new_space[0] + 70, new_space[1]))
                print(len(object_borders), len(self.object_locations))

            #Sets the 3 stars around the room
            self.star_locations = {}
            for i in range(3):
                new_space =  (random.choice(range(100, 900)), random.choice(range(100, 900)))
                self.star_locations[new_space] = ("minigame_assets/star.png", new_space[0], new_space[1])


label minigame(coin_nr=3, flashlight_nr=6):

    window hide 
    $ quick_menu = False

    call screen tutorial_screen()

    call screen stealth_minigame(coin_nr, flashlight_nr)

    call screen ending_screen(_return)

    $ quick_menu = True
    window show

    return 

screen tutorial_screen():
    add "bg minigame tutorial":
        blur 5

    vbox:
        xalign 0.5 yalign 0.5
        add "tutorial"
        textbutton _("Start"):
            xalign 0.5
            action Return(True)
    

# The end will return True if the game was won or False if game was lost
screen ending_screen(condition):
    add "bg minigame tutorial"
    add "bg end":
        xalign 0.5
        yalign 0.5
    vbox:
        xalign 0.5 yalign 0.5
        if condition == "won":
            text _("Congratulations, you won!")

            textbutton _("Continue"):
                action Return(True)
        else:
            text _("You lost! Would you like to try again?")
            null height 50
            textbutton _("Continue"):
                xalign 0.5
                action Return(False)
            textbutton _("Retry"):
                xalign 0.5
                action Jump("minigame")

        


screen stealth_minigame(coin_nr, flashlight_nr):
    add "bg minigame"
    add "bg minigame detail"
    default s_game = StealthGame(coin_nr, flashlight_nr)
    add s_game
    




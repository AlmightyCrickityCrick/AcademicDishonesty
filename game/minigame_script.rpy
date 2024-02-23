define dark = Character("Darkness")

init:
    image bg minigame = Frame("minigame_assets/bg minigame.png",  40, 40, 40, 40, tile=True)


init python:
    import random
    import pygame
    import math

    class PlayableSprite(renpy.Displayable):
        def __init__(self, chara_type, xpos, ypos, **properties):
            super(PlayableSprite, self).__init__(**properties)
            self.chara_type = chara_type
            self.img = "minigame_assets/companion.png" if(self.chara_type == "companion") else "minigame_assets/main_character.png"

            self.sprite = Transform(self.img)

            self.xpos = xpos
            self.ypos = ypos

            self.render_size = (1920, 1080)
                
        def attach_observer(self, observer):
            self.observer = observer
        
        def render(self, width, height, st, at):
            sprite_render = renpy.render(self.sprite, width, height, st, at)
            return sprite_render

        
        def event(self, ev, x, y, st):
            if (self.chara_type == "companion"):
                self.handle_companion_event(ev, x, y, st)
            else:
                self.handle_self_event(ev, x, y, st)
        
        def handle_companion_event(self, ev, x, y, st):
            if(ev.key == pygame.locals.K_RIGHT):
                self.xpos += 5
            elif(ev.key == pygame.locals.K_LEFT):
                self.xpos -= 5
            elif(ev.key == pygame.locals.K_UP):
                self.ypos -= 5
            elif(ev.key == pygame.locals.K_DOWN):
                self.ypos += 5
        
        def handle_self_event(self, ev, x, y, st):
            if(ev.key == pygame.locals.K_d):
                self.xpos += 5
            elif(ev.key == pygame.locals.K_a):
                self.xpos -= 5
            elif(ev.key == pygame.locals.K_w):
                self.ypos -= 5
            elif(ev.key == pygame.locals.K_s):
                self.ypos += 5
            
            self.observer.notify_obs("sound", self.xpos, self.ypos)



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
                
        def vision_cone(self):
            pass

        def sound_cone(self):
            pass

        def catch_cone(self):
            pass
        
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
                
                if(self.xpos != self.trigger_posx):
                    self.xpos += self.xdir * self.investigation_speed

                if (self.ypos != self.trigger_posy):
                    self.ypos += self.ydir * self.investigation_speed
                


                
        def random_move(self):
            return random.choice([-1, 0, 1]), random.choice([-1, 0, 1])

        def observe(self, playable):
            self.playable_list.append(playable)
            playable.attach_observer(self)
        
        def notify_obs(self, n_type , x, y):
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
            self.finish_x = 1000
            self.finish_y = 540

            self.object_reset()
            self.object_sprites = []
            for x in self.object_locations:
                self.object_sprites.append(Image(x[0], xsize= self.object_width, ysize = self.object_height))
            
            self.guard = GuardSprite()
            self.mc = PlayableSprite("main", 500, 50)
            self.companion = PlayableSprite("companion", 20, 80)

            self.guard.observe(self.mc)
            self.guard.observe(self.companion)

                
        
        
        def render(self, width, height, st, at):
            r = renpy.Render(self.render_size[0], self.render_size[1])
            for x in range(8):
                o_loc = self.object_locations[x]
                o_sprite = self.object_sprites[x]
                pi = renpy.render(o_sprite, 20, 20, st, at)
                r.blit(pi, (o_loc[1], o_loc[2]))
            
            #Trigger rending for the sprites
            x = self.guard.render(width, height, st, at)
            r.blit(x, (self.guard.xpos, self.guard.ypos))

            x = self.mc.render(width, height, st, at)
            r.blit(x, (self.mc.xpos, self.mc.ypos))

            x = self.companion.render(width, height, st, at)
            r.blit(x, (self.companion.xpos, self.companion.ypos))

            renpy.redraw(self, 0)
            return r

        
        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                self.mc.event(ev, x, y, st)
                self.companion.event(ev, x, y, st)
            

        
        def visit(self):
            child_list = self.object_sprites
            return child_list

        def object_reset(self):
            object_img = ["minigame_assets/plant.png", "minigame_assets/trashcan.png", "minigame_assets/sofa.png", "minigame_assets/vending_machine.png"]
            self.object_locations = []

            for i in range(8):
                self.object_locations.append((random.choice(object_img), random.randint(1, 80) * 10, random.randint(10, 100) * 10))



label minigame():

    e "Hello"
    call screen stealth_minigame
    
    return 

screen stealth_minigame():
    add "bg minigame"
    default s_game = StealthGame()
    add s_game

    text _("Yes")
    




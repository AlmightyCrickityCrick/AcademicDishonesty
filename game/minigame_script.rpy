define dark = Character("Darkness")

init:
    image bg minigame = Frame("minigame_assets/bg minigame.png",  40, 40, 40, 40, tile=True)


init python:
    import random
    import pygame


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
                
        
        
        def render(self, width, height, st, at):
            r = renpy.Render(self.render_size[0], self.render_size[1])
            for x in range(8):
                o_loc = self.object_locations[x]
                o_sprite = self.object_sprites[x]
                pi = renpy.render(o_sprite, 20, 20, st, at)
                r.blit(pi, (o_loc[1], o_loc[2]))

            renpy.redraw(self, 0)
            return r

        
        def event(self, ev, x, y, st):
            pass
        
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
    




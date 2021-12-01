import pygame, pyautogui ,sys
import time





pygame.init()
class Screen:
    def __init__(self, size, fps = 50):
        self.running = True
        self.name = ""
        self.size = size
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.events = pygame.event.get()
         

        self.window = pygame.display.set_mode(self.size)
        
        


    def screen_backend(self):
        self.clock.tick(self.fps)
        pygame.display.set_caption(self.name)

    
 
    def exit(self):
        # exit the screen
        self.running = False

    def quit_event(self  ):
            # anticipate a quit event

        for ev in self.events:
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                sys.exit()
    def dipslay_widgets(self):
        pass
    def show(self):
        while self.running:
            self.display_widgets()
            self.events = pygame.event.get()
            self.screen_backend()
             
            self.quit_event()
            pygame.display.update()
            


def text_to_gamer(  message, position, window, color, fontsize, font = 'chalkduster'):
        #### _this function  writes  a message to the user
    pygame.font.init()
    mess_obj = pygame.font.SysFont(font, fontsize)
    mess_render = mess_obj.render(message, 20, color)
    window.blit(mess_render, position)

def mouse_pos():
    pos = pyautogui.position()
    x = pos.x
    y = pos.y
    return(f"x = {x}  y = {y})")

class appScreen(Screen):
    def __init__(self):
        Screen.__init__(self,(300,300) )
        self.name = "Mouse Position Indicator"

    def display_widgets(self):
        self.window.fill(pygame.Color("black"))
        text_to_gamer(mouse_pos(), (50,150), self.window, pygame.Color("green"),40)

        
        
        
        
   



appScreen().show()
    

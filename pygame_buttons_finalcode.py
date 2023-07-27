import pygame
import pygame.gfxdraw
import keyboard


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()

background_colour = (234, 212, 252)
  
# Define the dimensions of
# screen object(width,height)

  
# Set the caption of the screen
pygame.display.set_caption('hi')
  
# Fill the background colour to the screen
screen.fill(background_colour)
  
# Update the display using flip
pygame.display.flip()
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size,
                 colors="",
                 hover_colors1="",
                 hover_colors2="",
                 hover_colors3="",
                 hover_colors4="",
                 style=1, borderc=(255, 255, 275),
                 command=lambda: print("No command activated for this button")):
        # the hover_colors attribute needs to be fixed
        super().__init__()
        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        if hover_colors1 == "":
            self.hover_colors1 = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors1 = hover_colors1
        if hover_colors2 == "":
            self.hover_colors2 = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors2 = hover_colors2
        if hover_colors3 == "":
            self.hover_colors3 = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors3 = hover_colors3
        if hover_colors4 == "":
            self.hover_colors4 = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors4 = hover_colors4
        self.style = style
        self.borderc = borderc  # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        buttons.add(self)
        self.buttons = []

    def render(self):
        self.text_render = self.font.render(self.text, 1, self.fg)
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        self.hover()
        self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150),
                         (self.x, self.y), (self.x + self.w, self.y), 5)
        pygame.draw.line(screen, (150, 150, 150),
                         (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y +
                         self.h), (self.x + self.w, self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w,
                         self.y + self.h), [self.x + self.w, self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w, self.h))

    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w, self.h))
        pygame.gfxdraw.rectangle(
            screen, (self.x, self.y, self.w, self.h), self.borderc)

    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''

        if keyboard.is_pressed("s"):
         
          self.colors = self.hover_colors1
          print("s")
          # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif keyboard.is_pressed("w"):
           self.colors=self.hover_colors2
        elif keyboard.is_pressed("a"):
           self.colors=self.hover_colors3
        elif keyboard.is_pressed("d"):
           self.colors = self.hover_colors4
        else:
           self.colors = self.original_colors

        self.render()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.pressed = 1


# FUNCTIONS for the buttons on click
# I used this convention ... on_+text of the button




def buttons_def():
    b0 = Button((125, 200), "Down", 55, "black on red", hover_colors1="black on green",
                )

    b1 = Button((150, 10), "Up", 55, "black on red",
                hover_colors2="black on green")

    b2 = Button((10, 100), "Left", 55, "black on red",
                hover_colors3="black on green",
                )
    b3 = Button((267, 100), "Right", 55, "black on red",
                hover_colors4="black on green",
                )

# ======================= this code is just for example, start the program from the main file
# in the main folder, I mean, you can also use this file only, but I prefer from the main file
# 29.8.2021


if __name__ == '__main__':
    pygame.init()
    game_on = 0

    def loop():
        # BUTTONS ISTANCES
        game_on = 1
        buttons_def()
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = 0
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        game_on = 0
            if game_on:
                buttons.update()
                buttons.draw(screen)
            else:
                pygame.quit()
                sys.exit()
            buttons.draw(screen)
            clock.tick(60)
            pygame.display.update()
        pygame.quit()

    loop()

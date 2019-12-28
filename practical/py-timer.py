import psutil, time, datetime, pygame

pygame.init()

def time_since_boot():
    return str(datetime.timedelta(seconds=int(time.time() - psutil.boot_time())))

#general constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FRAME_RATE = 30
WHITE = ((255, 255, 255))
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

font = pygame.font.Font("3Dumb.ttf", 100)

def write_timer(timer):
    timer = font.render(timer, True, WHITE)
    timer_rect = timer.get_rect()
    timer_rect.center = (500, 300)
    screen.blit(timer, timer_rect)

class Game():
    def __init__(self):
        pass

    def loop(self, screen):
        clock = pygame.time.Clock()

        while True:
            delta_t = clock.tick( FRAME_RATE )

            # handle input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return # closing the window, end of the game loop

            # render game screen
            screen.fill( (0, 0, 0) ) # black background
            write_timer(time_since_boot())

            # update display
            pygame.display.update()
            # or pygame.display.flip()

    def quit(self):
        pass


def main():
    pygame.display.set_caption( 'Time on Pi ' )
    #pygame.mouse.set_visible( False )

    game = Game()
    game.loop( screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()


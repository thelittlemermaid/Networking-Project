# import the pygame module, so you can use it
import pygame



icon = pygame.image.load('cardImages/icon.png')
cBack = pygame.image.load('cardImages/cards/cardback.png')
diamondA = pygame.image.load('cardImages/cards/ad.png')
clubA = pygame.image.load('cardImages/cards/ac.png')
heartA = pygame.image.load('cardImages/cards/ah.png')
spadeA = pygame.image.load('cardImages/cards/as.png')
diamond2 = pygame.image.load('cardImages/cards/2d.png')
club2 = pygame.image.load('cardImages/cards/2c.png')
heart2 = pygame.image.load('cardImages/cards/2h.png')
spade2 = pygame.image.load('cardImages/cards/2s.png')
diamond3 = pygame.image.load('cardImages/cards/3d.png')
club3 = pygame.image.load('cardImages/cards/3c.png')
heart3 = pygame.image.load('cardImages/cards/3h.png')
spade3 = pygame.image.load('cardImages/cards/3s.png')
diamond4 = pygame.image.load('cardImages/cards/4d.png')
club4 = pygame.image.load('cardImages/cards/4c.png')
heart4 = pygame.image.load('cardImages/cards/4h.png')
spade4 = pygame.image.load('cardImages/cards/4s.png')
diamond5 = pygame.image.load('cardImages/cards/5d.png')
club5 = pygame.image.load('cardImages/cards/5c.png')
heart5 = pygame.image.load('cardImages/cards/5h.png')
spade5 = pygame.image.load('cardImages/cards/5s.png')
diamond6 = pygame.image.load('cardImages/cards/6d.png')
club6 = pygame.image.load('cardImages/cards/6c.png')
heart6 = pygame.image.load('cardImages/cards/6h.png')
spade6 = pygame.image.load('cardImages/cards/6s.png')
diamond7 = pygame.image.load('cardImages/cards/7d.png')
club7 = pygame.image.load('cardImages/cards/7c.png')
heart7 = pygame.image.load('cardImages/cards/7h.png')
spade7 = pygame.image.load('cardImages/cards/7s.png')
diamond8 = pygame.image.load('cardImages/cards/8d.png')
club8 = pygame.image.load('cardImages/cards/8c.png')
heart8 = pygame.image.load('cardImages/cards/8h.png')
spade8 = pygame.image.load('cardImages/cards/8s.png')
diamond9 = pygame.image.load('cardImages/cards/9d.png')
club9 = pygame.image.load('cardImages/cards/9c.png')
heart9 = pygame.image.load('cardImages/cards/9h.png')
spade9 = pygame.image.load('cardImages/cards/9s.png')
diamond10 = pygame.image.load('cardImages/cards/10d.png')
club10 = pygame.image.load('cardImages/cards/10c.png')
heart10 = pygame.image.load('cardImages/cards/10h.png')
spade10 = pygame.image.load('cardImages/cards/10s.png')
diamondJ = pygame.image.load('cardImages/cards/jd.png')
clubJ = pygame.image.load('cardImages/cards/jc.png')
heartJ = pygame.image.load('cardImages/cards/jh.png')
spadeJ = pygame.image.load('cardImages/cards/js.png')
diamondQ = pygame.image.load('cardImages/cards/qd.png')
clubQ = pygame.image.load('cardImages/cards/qc.png')
heartQ = pygame.image.load('cardImages/cards/qh.png')
spadeQ = pygame.image.load('cardImages/cards/qs.png')
diamondK = pygame.image.load('cardImages/cards/kd.png')
clubK = pygame.image.load('cardImages/cards/kc.png')
heartK = pygame.image.load('cardImages/cards/kh.png')
spadeK = pygame.image.load('cardImages/cards/ks.png')
green = pygame.image.load('cardImages/green.png')

# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("cardImages/icon_full.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("War Card Game")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((640,480))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        screen.blit(green, (0,0))
        screen.blit(diamondA, (50,50))
        screen.blit(clubA, (80, 50))
        screen.blit(clubK, (50, 300))
        screen.blit(spadeK, (80, 300))

        pygame.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

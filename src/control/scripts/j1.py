import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

while 1:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        name = joystick.get_name()
        print "Joystick name: ",name

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        print "Number of axes: ",axes

        for i in range( axes ):
            axis = joystick.get_axis( i )
            print "Axis value: ",i, axis

        buttons = joystick.get_numbuttons()
        print "Number of buttons: ",buttons

        for i in range( buttons ):
            button = joystick.get_button( i )
            print "Button value: ",i,button

        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        print "Number of hats: ",hats

        for i in range( hats ):
            hat = joystick.get_hat( i )
            print "Hat value: ",i, str(hat)


    # Limit to 20 frames per second
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()

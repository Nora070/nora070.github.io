import pygame
import visualize
from visualize import ActivationRecord, draw_program_code

program1_records = [
    ActivationRecord('AR: Main', 'main', None, 'p=2', 'OS', None, None, 0),
    ActivationRecord('AR: fun1', 'fun1', 'r=2', 's, t', 'main', 'main AR', 'main AR', 1),
    ActivationRecord('AR: fun2', 'fun2', 'x=s', 'y', 'fun1', 'fun1 AR', 'main AR', 2),
    ActivationRecord('AR: fun3', 'fun3', 'q=y', None, 'fun2', 'fun2 AR', 'main AR', 3)
]

program2_records = [
    ActivationRecord('AR: Main', 'main', None, 'value', 'OS', None, None, 0),
    ActivationRecord('AR: factorial(3)', 'factorial', 'n=3', None, 'main', 'main AR', 'main AR', 1),
    ActivationRecord('AR: factorial(2)', 'factorial', 'n=2', None, 'factorial(3)', 'factorial(3) AR', 'factorial(3) AR', 2),
    ActivationRecord('AR: factorial(1)', 'factorial', 'n=1', None, 'factorial(2)', 'factorial(2) AR', 'factorial(2) AR', 3)
]

program3_records = [
    ActivationRecord('AR: Main', 'main', None, 'x', 'OS', None, None, 0),
    ActivationRecord('AR: bigsub', 'bigsub', None, 'a, b, c', 'main', 'main AR', 'main AR', 1),
    ActivationRecord('AR: sub2', 'sub2', 'x=7', 'b, e', 'bigsub', 'bigsub AR', 'bigsub AR', 2),
    ActivationRecord('AR: sub3', 'sub3', None, 'c, e', 'sub2', 'sub2 AR', 'sub2 AR', 3),
    ActivationRecord('AR: sub1', 'sub1', None, 'a, d', 'sub3', 'sub3 AR', 'bigsub AR', 4)
]

slides = [ #list of what order for things to disply
    ('code', visualize.PROGRAM1_CODE),
    ('ar', program1_records[0]),
    ('ar', program1_records[1]),
    ('ar', program1_records[2]),
    ('ar', program1_records[3]),
    
    # Program 2
    ('code', visualize.PROGRAM2_CODE),
    ('ar', program2_records[0]),
    ('ar', program2_records[1]),
    ('ar', program2_records[2]),
    ('ar', program2_records[3]),
    
    # Program 3
    ('code', visualize.PROGRAM3_CODE),
    ('ar', program3_records[0]),
    ('ar', program3_records[1]),
    ('ar', program3_records[2]),
    ('ar', program3_records[3]),
    ('ar', program3_records[4])
    
] 


current_slide = 0
current_code = visualize.PROGRAM1_CODE #default program code
current_ars = [] #list of current activation records

running = True
clock = pygame.time.Clock()

while running:
    visualize.screen.fill((252, 204, 250))
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #space bar to go to next animation
                    
                    # Check what the current slide is
                    slide_type, slide_content = slides[current_slide]
                    
                    if slide_type == 'code':
                        # New program - clear everything and show code
                        current_code = slide_content
                        current_ars = []
                    elif slide_type == 'ar':
                        # Add new activation record to the list
                        current_ars.append(slide_content)
    
                    current_slide += 1 #move to next slide
                    
                    if current_slide >= len(slides):
                       # print("Length of slides:", len(slides))
                       # print("Current slide index:", current_slide)
                        pygame.quit() #current_slide = 0  # Loop back to start
                        exit()
                    
    #outside of the event loop, so it draws repeatedly and not only when key is pressed
    if current_code:
        draw_program_code(current_code)
    
    # Draw all current ARs
    for ar in current_ars:
        ar.animate()
        ar.draw()
    
    pygame.display.flip()
    clock.tick(60)                
        
    
pygame.quit()
import pygame
from random import randrange, randint


# Define some colors
BACKGROUND_COLOR = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        # I chose to have extra much blue (B) in the RGB color
        self.color = randrange(30, 100), randrange(30, 100), randrange(50, 256)
        self.dx = randint(-3, 3)
        self.dy = randint(-3, 3)


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Balls")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        balls.append(Ball(100*i, 100*i, randrange(10, 40)))

    # Loop until the user clicks the close button or ESC.
    done = False
    while not done:
        # Limit number of frames per second
        clock.tick(60)

        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        for ball in balls:
            min_x = min_y = ball.radius
            max_x = SCREEN_WIDTH - ball.radius
            max_y = SCREEN_HEIGHT - ball.radius
            ball.x = constrain(min_x, ball.x + ball.dx, max_x)
            ball.y = constrain(min_y, ball.y + ball.dy, max_y)
            # Bounce?
            if ball.x in (min_x, max_x):
                ball.dx = -ball.dx
            if ball.y in (min_y, max_y):
                ball.dy = -ball.dy

        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()


def constrain(small, value, big):
    """Return a new value which isn't smaller than small or larger than big"""
    return min(max(value, small), big)


if __name__ == "__main__":
    main()

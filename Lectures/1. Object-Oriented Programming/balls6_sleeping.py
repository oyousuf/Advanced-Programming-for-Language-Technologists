import pygame
from random import randrange, randint, choice, random


# Define some colors
BACKGROUND_COLOR = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.randomize()
        self.set_minmax()

    def set_minmax(self):
        self.min_x = self.min_y = self.radius
        self.max_x = SCREEN_WIDTH - self.radius
        self.max_y = SCREEN_HEIGHT - self.radius

    def randomize(self):
        # I chose to have extra much blue (B) in the RGB color
        self.color = randrange(30, 100), randrange(30, 100), randrange(50, 256)
        self.dx = randint(-3, 3)
        self.dy = randint(-3, 3)

    def move(self):
        self.x = constrain(self.min_x, self.x + self.dx, self.max_x)
        self.y = constrain(self.min_y, self.y + self.dy, self.max_y)
        # Bounce?
        if self.x in (self.min_x, self.max_x):
            self.dx = -self.dx
        if self.y in (self.min_y, self.max_y):
            self.dy = -self.dy


class SpecialBall(Ball):
    color = 250, 20, 20
    radius = 8

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.set_direction()
        self.sleeping = 1
        self.set_minmax()

    def set_direction(self):
        speed = randint(4, 6)
        self.dx = choice((-1, 1)) * speed
        self.dy = choice((-1, 1)) * speed

    def move(self):
        if self.sleeping > 0:
            self.sleeping -= 1
            if self.sleeping == 0:
                self.set_direction()
        else:
            # super().move()
            Ball.move(self)
            if random() < 0.01:
                self.sleeping = 100

class Player:
    def __init__(self):
        # Start near a corner
        self.x = 30
        self.y = SCREEN_HEIGHT - 30
        self.radius = 10
        self.color = (0, 0, 0)

    def move(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1
        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        min_x, min_y = self.radius, self.radius
        max_x = SCREEN_WIDTH - self.radius
        max_y = SCREEN_HEIGHT - self.radius
        self.x = constrain(min_x, self.x + dx, max_x)
        self.y = constrain(min_y, self.y + dy, max_y)


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Balls")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        balls.append(Ball(100*i, 100*i, randrange(10, 40)))

    player = Player()

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
                elif event.key == pygame.K_r:
                    choice(balls).randomize()
                elif event.key == pygame.K_a:
                    # The instructions didn't say what radius the new balls
                    # should have. I use a random value.
                    new_ball = Ball(150, 200, randrange(10, 40))
                    balls.append(new_ball)
                elif event.key == pygame.K_s:
                    new_ball = SpecialBall(150, 200)
                    balls.append(new_ball)

        for ball in balls:
            ball.move()

        player.move()

        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)
        pygame.draw.circle(screen, player.color,
                           (player.x, player.y), player.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()


def constrain(small, value, big):
    """Return a new value which isn't smaller than small or larger than big"""
    return min(max(value, small), big)


if __name__ == "__main__":
    main()
